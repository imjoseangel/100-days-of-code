#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=C0111, R0902, R0903, R0912

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from azure.datalake.store import core, lib
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
    - Create or delete an ACLl within a given directory in a Datalake.
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
    object_id:
        description: The object if of a user, service principal or security group in AAD for the vault. # noqa: E501
        required: true
        type: str
    permissions:
        description:
            - Required if C(state=present).
        type: str
        choices: [ 'r--', '-w-', '--x', 'rw-', 'r-x', '-wx', 'rwx' ]
    acl_spec:
        description:
            - The ACL specification to use in modifying/removing the ACL at the path
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
        path: /raw
        store_name: mydatalake
        object_id: myserviceprincipalid
        permissions: 'r-x'
        acl_spec: "default:user"

    - name: Delete acl for raw dir
      azure_rm_datalakeacl:
        path: /raw
        store_name: mydatalake
        object_id: myserviceprincipalid
        acl_spec: "default:user"
        state:absent
'''

RETURN = '''
permissions:
  description: Current Directory Permissions
  returned: always
  type: str
state:
  description: Current Directory Permissions
  returned: always
  type: str
  sample: created
'''


class Actions:
    NoAction, Create, Delete = range(3)


class AzureRMDataLakes(AzureRMModuleBase):
    """Configuration class for an Azure RM Application Gateway resource"""
    def __init__(self):
        self.module_arg_spec = dict(store_name=dict(type='str', required=True),
                                    dir_name=dict(type='str', required=True),
                                    object_id=dict(type='str', required=True),
                                    permissions=dict(type='str',
                                                     required=False,
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
                                    recursive=dict(type='bool',
                                                   required=False,
                                                   default=False),
                                    state=dict(type='str',
                                               default='present',
                                               choices=['present', 'absent']))

        self.module_required_if = [['state', 'present', ['permissions']]]

        self.dir_name = None
        self.store_name = None
        self.permissions = None
        self.object_id = None
        self.acl_spec = None
        self.recursive = False
        self.resource = 'https://datalake.azure.net/'

        self.results = dict(changed=False)
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDataLakes,
              self).__init__(derived_arg_spec=self.module_arg_spec,
                             supports_check_mode=True,
                             supports_tags=False)

    def exec_module(self, **kwargs):

        for key in list(self.module_arg_spec.keys()) + ['tags']:
            setattr(self, key, kwargs[key])

        # Access to the data lake
        adl_creds = self.get_adlcreds()

        old_response = None
        response = None

        old_response = self.find_objectid(adl_creds)

        if not old_response:
            self.log("Datalake permission doesn't exist")
            if self.state == 'absent':
                self.log("Old permnission didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("Datalake permission already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                pass

        if self.to_do == Actions.Create:
            self.log("Need to Create / Update the Datalake permission")

            if self.check_mode:
                self.results['changed'] = True
                self.results['state'] = 'created (check_mode)'
                return self.results

            response = self.create_update_acl(adl_creds)

            if not old_response:
                self.results['changed'] = True
                self.results['state'] = 'created'
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")

        elif self.to_do == Actions.Delete:
            self.log("Datalake permission deleted")
            self.results['changed'] = True
            self.results['state'] = 'deleted'

            if self.check_mode:
                self.results['state'] = 'deleted (check_mode)'
                return self.results

            self.remove_acl(adl_creds)

        else:
            self.log("Datalake permission unchanged")
            self.results['changed'] = False
            self.results['state'] = 'unchanged'
            response = old_response

        if Actions.Create:
            self.results["permissions"] = "{0}:{1}:{2}".format(
                self.acl_spec, self.object_id, self.permissions)
        else:
            self.results['permissions'] = "{0}:{1}".format(
                self.acl_spec, self.object_id)

        return self.results

    def get_adlcreds(self):

        try:
            adl_creds = lib.auth(tenant_id=self.credentials['tenant'],
                                 client_secret=self.credentials['secret'],
                                 client_id=self.credentials['client_id'],
                                 resource=self.resource)

            adls_accountname = self.store_name
            adls_filesystemclient = core.AzureDLFileSystem(
                adl_creds, store_name=adls_accountname)

        except CloudError as exc:
            self.log('Error attempting to access to the Data lake instance.')
            self.fail("Error login to the Data Lake instance: {0}".format(
                str(exc)))

        return adls_filesystemclient

    def find_objectid(self, creds):

        acl_status = creds.get_acl_status(self.dir_name)

        acl_match = [
            object_id for object_id in acl_status['entries']
            if self.object_id in object_id
        ]

        return acl_match

    def create_update_acl(self, creds):

        try:
            acl_modify = creds.modify_acl_entries(
                self.dir_name,
                "{0}:{1}:{2}".format(self.acl_spec, self.object_id,
                                     self.permissions),
                recursive=self.recursive)

        except CloudError as exc:
            self.log(
                'Error attempting to update acls to the Data lake instance.')
            self.fail("Error updating Data Lake acls: {0}".format(str(exc)))

        return acl_modify

    def remove_acl(self, creds):
        try:
            acl_remove = creds.remove_acl_entries(self.dir_name,
                                                  "{0}:{1}".format(
                                                      self.acl_spec,
                                                      self.object_id),
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
