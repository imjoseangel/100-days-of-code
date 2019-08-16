#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=C0111, R0902, R0903, R0912, C0301, R0801

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from datetime import datetime
    from datetime import timezone
    import uuid
    from azure.common.credentials import ServicePrincipalCredentials
    from azure.graphrbac import GraphRbacManagementClient
    from azure.graphrbac.models import ApplicationCreateParameters
    from azure.graphrbac.models import PasswordCredential
    from azure.graphrbac.models import ServicePrincipalCreateParameters
    from azure.graphrbac.models.graph_error import GraphErrorException
    from msrestazure.azure_cloud import AZURE_PUBLIC_CLOUD
    # from msrestazure.azure_exceptions import CloudError
except ImportError:
    # This is handled in azure_rm_common
    pass

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: azure_rm_appregistration
version_added: 2.8
short_description: Registers Azure Application
description:
    - Create or delete an application with a service principal in Azure given an application Name. # noqa: E501
options:
    sp_name:
        description: Name of the application and service principal.
        required: true
        type: str
    multitenant:
        description: Specifies if is a multitenant application or not.
        type: bool
        default: false
    state:
        description:
            - Assert the state of the application. Use C(present) to create an application and C(absent) to delete an application. # noqa: E501
        default: present
        choices:
            - absent
            - present

extends_documentation_fragment:
    - azure

author:
    - Jose Angel Munoz (@imjoseangel)

'''

EXAMPLES = '''
    - name: Create application
      azure_rm_appregistration:
        sp_name: myserviceprincipalid

    - name: Delete acl for raw dir
      azure_rm_appregistration:
        sp_name: myserviceprincipalid
        state: absent
'''

RETURN = '''
client_id:
  description: Application Client ID
  returned: always
  type: str
  sample: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxxx
object_id:
  description: Application Object ID
  returned: always
  type: str
  sample: sample: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxxx
sp_id:
  description: Service Principal Object ID
  returned: 'on creation'
  type: str
  sample: sample: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxxx
tenant_id:
  description: Application Tenant ID
  returned: 'if exists'
  type: str
  sample: sample: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxxx
secret:
  description: Application Secret
  returned: 'on creation'
  type: str
  sample: sample: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxxx
'''


class AzureRMServicePrincipal(AzureRMModuleBase):
    """Configuration class for an Azure RM Application Gateway resource"""
    def __init__(self):
        self.module_arg_spec = dict(sp_name=dict(type='str', required=True),
                                    multitenant=dict(type='bool',
                                                     default=False),
                                    state=dict(type='str',
                                               default='present',
                                               choices=['present', 'absent']))

        self.sp_name = None
        self.results = dict(changed=False)
        self.state = None
        self.multitenant = None

        super(AzureRMServicePrincipal,
              self).__init__(derived_arg_spec=self.module_arg_spec,
                             supports_check_mode=True,
                             supports_tags=False)

    def exec_module(self, **kwargs):

        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])

        results = dict()
        changed = False

        sp_creds, tenant = self.get_spcreds()

        try:
            results['client_id'], results['object_id'], _ = self.get_objectid(
                sp_creds)
            results['tenant_id'] = tenant

            # Key exists and will be deleted
            if self.state == 'absent':
                changed = True

        except TypeError:
            # App doesn't exist
            if self.state == 'present':
                changed = True

        self.results['changed'] = changed
        self.results['state'] = results

        if not self.check_mode:

            # Create App
            if self.state == 'present' and changed:
                results['client_id'], results['object_id'], results[
                    'secret'], results['sp_id'] = self.create_sp(sp_creds)
                self.results['state'] = results
                self.results['state']['status'] = 'Created'
            # Delete App
            elif self.state == 'absent' and changed:
                self.delete_sp(sp_creds, results['object_id'])
                self.results['state'] = results
                self.results['state']['status'] = 'Deleted'
        else:
            if self.state == 'present' and changed:
                self.results['state']['status'] = 'Created'
            elif self.state == 'absent' and changed:
                self.results['state']['status'] = 'Deleted'

        return self.results

    def get_spcreds(self):

        if 'client_id' not in self.credentials or 'secret' not in self.credentials or self.credentials[  # noqa: E501
                'client_id'] is None or self.credentials['secret'] is None:
            self.fail(
                'Please specify client_id, secret and tenant to manage Service Principals'  # noqa: E501
            )

        tenant = self.credentials.get('tenant')
        if not self.credentials['tenant']:
            tenant = "common"

        sp_creds = ServicePrincipalCredentials(
            client_id=self.credentials['client_id'],
            secret=self.credentials['secret'],
            tenant=tenant,
            resource="https://graph.windows.net")

        graph_rbac_client = GraphRbacManagementClient(
            sp_creds,
            tenant,
            base_url=AZURE_PUBLIC_CLOUD.endpoints.
            active_directory_graph_resource_id)

        return graph_rbac_client, tenant

    def get_objectid(self, creds):

        try:
            application = next(
                creds.applications.list(
                    filter="identifierUris/any(c:c eq 'http://{}.com')".format(
                        self.sp_name)))

            service_principal = next(
                creds.service_principals.list(
                    filter="appId eq '{}'".format(application.app_id)))

            return application.app_id, application.object_id, \
                service_principal.object_id

        except StopIteration:
            pass

    def create_sp(self, creds):

        application_credential = uuid.uuid4()

        try:
            display_name = self.sp_name

            application = creds.applications.create(
                parameters=ApplicationCreateParameters(
                    available_to_other_tenants=self.multitenant,
                    identifier_uris=["http://{}.com".format(display_name)],
                    display_name=display_name,
                    password_credentials=[
                        PasswordCredential(end_date=datetime(
                            2299, 12, 31, 0, 0, 0, 0, tzinfo=timezone.utc),
                                           value=application_credential,
                                           key_id=uuid.uuid4())
                    ]))
            service_principal = creds.service_principals.create(
                ServicePrincipalCreateParameters(app_id=application.app_id,
                                                 account_enabled=True))
        except GraphErrorException as rbac_exception:
            if rbac_exception.inner_exception.code == "Request_BadRequest":
                application = next(
                    creds.applications.list(
                        filter="identifierUris/any(c:c eq 'http://{}.com')".
                        format(display_name)))

                service_principal = next(
                    creds.service_principals.list(
                        filter="appId eq '{}'".format(application.app_id)))
            else:
                raise rbac_exception

        return application.app_id, application.object_id, str(
            application_credential), service_principal.object_id

    @staticmethod
    def delete_sp(creds, appobjectid):
        try:
            creds.applications.delete(appobjectid)

        except GraphErrorException as rbac_exception:
            raise rbac_exception


def main():
    """Main execution"""
    AzureRMServicePrincipal()


if __name__ == '__main__':
    main()
