#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=C0111, R0902, R0903, R0912, C0301, R0801

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import re
from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from azure.datalake.store import core, lib
    from azure.common.credentials import ServicePrincipalCredentials
    from azure.graphrbac import GraphRbacManagementClient
    from msrestazure.azure_cloud import AZURE_PUBLIC_CLOUD
    from msrestazure.azure_exceptions import CloudError
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
module: azure_rm_dataleakacl
version_added: 2.8
short_description: Setup Azure Datalake ACLs
description:
    - Create or delete an ACL within a given directory in a Datalake.
options:
    store_name:
        description:
            - Name of the Datalake.
        required: true
        type: str
    dir_name:
        description:
            - Name of the Datalake directory.
        required: true
        type: str
    sp_name:
        description: Name or object id of the application for the acl.
        required: true
        type: str
    permissions:
        description:
            - Required if C(state=present).
        type: str
        choices: [ 'r--', '-w-', '--x', 'rw-', 'r-x', '-wx', 'rwx' ]
    acl_spec:
        description:
            - The ACL specification to use in modifying/removing the ACL at the path # noqa: E501
        required: true
        type: str
        choices: [ 'user', 'group', 'other', 'default:user', 'default:group', 'default:other' ]
    recursive:
        description: Specifies whether to modify ACLs recursively or not
        type: bool
        default: false
        required: false
    state:
        description:
            - Assert the state of the acl. Use C(present) to create an acl and C(absent) to delete an acl.
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
    - name: Create acl for raw dir
      azure_rm_datalakeacl:
        dir_name: /raw
        store_name: mydatalake
        sp_name: myserviceprincipalid
        permissions: 'r-x'
        acl_spec: "default:user"

    - name: Delete acl for raw dir
      azure_rm_datalakeacl:
        dir_name: /raw
        store_name: mydatalake
        sp_name: myserviceprincipalid
        acl_spec: "default:user"
        state:absent
'''

RETURN = '''
acl:
  description: Current Directory Permissions
  returned: always
  type: str
operation:
  description: ACLs changed over directory
  returned: always
  type: str
  sample: user:mytestuser:r-x
'''


class Actions:
    NoAction, Create, Delete = range(3)


class AzureRMDataLakes(AzureRMModuleBase):
    """Configuration class for an Azure RM Application Gateway resource"""
    def __init__(self):
        self.module_arg_spec = dict(store_name=dict(type='str', required=True),
                                    dir_name=dict(type='path', required=True),
                                    sp_name=dict(type='str', required=True),
                                    permissions=dict(type='str',
                                                     choices=[
                                                         'r--', '-w-', '--x',
                                                         'rw-', 'r-x', '-wx',
                                                         'rwx'
                                                     ]),
                                    acl_spec=dict(type='str',
                                                  required=True,
                                                  choices=[
                                                      'user', 'group', 'other',
                                                      'default:user',
                                                      'default:group',
                                                      'default:other'
                                                  ]),
                                    recursive=dict(type='bool', default=False),
                                    state=dict(type='str',
                                               default='present',
                                               choices=['present', 'absent']))

        self.module_required_if = [['state', 'present', ['permissions']]]

        self.dir_name = None
        self.store_name = None
        self.permissions = None
        self.sp_name = None
        self.acl_spec = None
        self.recursive = False
        self.resource = 'https://datalake.azure.net/'
        self.state = None
        self.results = dict(changed=False)

        super(AzureRMDataLakes,
              self).__init__(derived_arg_spec=self.module_arg_spec,
                             supports_check_mode=True,
                             supports_tags=False,
                             required_if=self.module_required_if)

    def exec_module(self, **kwargs):

        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])

        results = dict()
        changed = False

        # Access to the data lake
        adl_creds, sp_creds = self.get_adlcreds()

        try:

            pattern = re.compile(
                "[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[34][0-9a-fA-F]{3}-[89ab]\
                    [0-9a-fA-F]{3}-[0-9a-fA-F]{12}")

            if pattern.match(self.sp_name):
                results['object_id'] = sp_id = self.sp_name
            else:
                results['object_id'] = sp_id = self.get_objectid(sp_creds)

            results['acl'] = self.get_acls(adl_creds, sp_id)

            # Key exists and will be deleted
            if self.state == 'absent':
                changed = True

        except TypeError:
            # AC: doesn't exist
            if self.state == 'present':
                changed = True

        self.results['changed'] = changed
        self.results['state'] = results

        if not self.check_mode:

            # Create ACL
            if self.state == 'present' and changed:
                results['operation'] = self.create_acl(adl_creds)
                self.results['state'] = results
                self.results["permissions"] = "{0}:{1}:{2}".format(
                    self.acl_spec, self.sp_name, self.permissions)
                self.results['state']['status'] = 'Created'
            # Delete ACL
            elif self.state == 'absent' and changed:
                self.delete_acl(adl_creds)
                self.results['state'] = results
                self.results['permissions'] = "{0}:{1}".format(
                    self.acl_spec, self.sp_name)
                self.results['state']['status'] = 'Deleted'
        else:
            if self.state == 'present' and changed:
                self.results['state']['status'] = 'Created'
            elif self.state == 'absent' and changed:
                self.results['state']['status'] = 'Deleted'

        return self.results

    def get_adlcreds(self):

        if 'client_id' not in self.credentials or 'secret' not in self.credentials or self.credentials[  # noqa: E501
                'client_id'] is None or self.credentials['secret'] is None:
            self.fail(
                'Please specify client_id, secret and tenant to access azure Data Lake.'  # noqa: E501
            )

        tenant = self.credentials.get('tenant')
        if not self.credentials['tenant']:
            tenant = "common"

        adl_creds = lib.auth(tenant_id=tenant,
                             client_secret=self.credentials['secret'],
                             client_id=self.credentials['client_id'],
                             resource=self.resource)

        adls_accountname = self.store_name
        adls_filesystemclient = core.AzureDLFileSystem(
            adl_creds, store_name=adls_accountname)

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

        return adls_filesystemclient, graph_rbac_client

    def get_acls(self, creds, sp_id):

        acl_status = creds.get_acl_status(self.dir_name)

        if self.state == 'present':
            match_string = "{0}:{1}:{2}".format(self.acl_spec, sp_id,
                                                self.permissions)
        else:
            match_string = "{0}:{1}".format(self.acl_spec, sp_id)

        acl_matching = [
            sp_name for sp_name in acl_status['entries']
            if match_string in sp_name
        ]

        if acl_matching:
            return next(iter(acl_matching))

        raise TypeError

    def get_objectid(self, creds):

        try:
            application = next(
                creds.applications.list(
                    filter="displayName eq '{}'".format(self.sp_name)))

            service_principal = next(
                creds.service_principals.list(
                    filter="appId eq '{}'".format(application.app_id)))

            return service_principal.object_id

        except StopIteration:
            raise TypeError

    def create_acl(self, creds):

        try:
            acl_modify = creds.modify_acl_entries(
                self.dir_name,
                "{0}:{1}:{2}".format(self.acl_spec, self.sp_name,
                                     self.permissions),
                recursive=self.recursive)

        except CloudError as exc:
            self.log(
                'Error attempting to update acls to the Data lake instance.')
            self.fail("Error updating Data Lake acls: {0}".format(str(exc)))

        return acl_modify

    def delete_acl(self, creds):
        try:
            acl_remove = creds.remove_acl_entries(self.dir_name,
                                                  "{0}:{1}".format(
                                                      self.acl_spec,
                                                      self.sp_name),
                                                  recursive=self.recursive)

        except CloudError as exc:
            self.log(
                'Error attempting to removing acls to the Data lake instance.')
            self.fail("Error removing Data Lake acls: {0}".format(str(exc)))

        return acl_remove


def main():
    """Main execution"""
    AzureRMDataLakes()


if __name__ == '__main__':
    main()
