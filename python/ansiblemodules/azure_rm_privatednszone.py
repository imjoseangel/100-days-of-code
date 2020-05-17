#!/usr/bin/python
#
# Copyright (c) 2020 Jose Angel Munoz, <josea.munoz@gmail.com>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: azure_rm_privatednszone

version_added: "2.10"

short_description: Manage Azure private DNS zones

description:
    - Creates and deletes Azure private DNS zones.

options:
    resource_group:
        description:
            - name of resource group.
        required: true
    name:
        description:
            - Name of the private DNS zone.
        required: true
    state:
        description:
            - Assert the state of the zone. Use C(present) to create or update and C(absent) to delete.
        default: present
        choices:
            - absent
            - present

extends_documentation_fragment:
    - azure.azcollection.azure
    - azure.azcollection.azure_tags

author:
    - Jose Angel Munoz (@imjoseangel)
'''

EXAMPLES = '''

- name: Create a private DNS zone
  azure_rm_privatednszone:
    resource_group: myResourceGroup
    name: example.com

- name: Delete a private DNS zone
  azure_rm_privatednszone:
    resource_group: myResourceGroup
    name: example.com
    state: absent

'''

RETURN = '''
state:
    description:
        - Current state of the zone.
    returned: always
    type: dict
    sample: {
        "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroup/myResourceGroup",
        "location": "global",
        "name": "Testing",
        "number_of_record_sets": 2,
        "number_of_virtual_network_links": 0,
        "number_of_virtual_network_links_with_registration": 0
    }

'''

from ansible_collections.azure.azcollection.plugins.module_utils.azure_rm_common import AzureRMModuleBase, format_resource_id
from ansible.module_utils._text import to_native

try:
    from msrestazure.azure_exceptions import CloudError
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMPrivateDNSZone(AzureRMModuleBase):
    def __init__(self):

        # define user inputs from playbook
        self.module_arg_spec = dict(resource_group=dict(type='str',
                                                        required=True),
                                    name=dict(type='str', required=True),
                                    state=dict(choices=['present', 'absent'],
                                               default='present',
                                               type='str'))

        # store the results of the module operation
        self.results = dict(changed=False, state=dict())

        self.resource_group = None
        self.name = None
        self.state = None
        self.tags = None

        super(AzureRMPrivateDNSZone, self).__init__(self.module_arg_spec,
                                                    supports_check_mode=True,
                                                    supports_tags=True)

    def exec_module(self, **kwargs):

        # create a new zone variable in case the 'try' doesn't find a zone
        zone = None
        for key in list(self.module_arg_spec.keys()) + ['tags']:
            setattr(self, key, kwargs[key])

        self.results['check_mode'] = self.check_mode

        # retrieve resource group to make sure it exists
        self.get_resource_group(self.resource_group)

        changed = False
        results = dict()

        try:
            self.log('Fetching private DNS zone {0}'.format(self.name))
            zone = self.private_dns_client.private_zones.get(
                self.resource_group, self.name)

            # serialize object into a dictionary
            results = zone_to_dict(zone)

            # don't change anything if creating an existing zone, but change if deleting it
            if self.state == 'present':
                changed = False

                update_tags, results['tags'] = self.update_tags(
                    results['tags'])
                if update_tags:
                    changed = True
            elif self.state == 'absent':
                changed = True

        except CloudError:
            # the zone does not exist so create it
            if self.state == 'present':
                changed = True
            else:
                # you can't delete what is not there
                changed = False

        self.results['changed'] = changed
        self.results['state'] = results

        # return the results if your only gathering information
        if self.check_mode:
            return self.results

        if changed:
            if self.state == 'present':
                zone = self.private_dns_models.PrivateZone(tags=self.tags,
                                                           location='global')
                self.results['state'] = self.create_or_update_zone(zone)
            elif self.state == 'absent':
                # delete zone
                self.delete_zone()
                # the delete does not actually return anything. if no exception, then we'll assume
                # it worked.
                self.results['state']['status'] = 'Deleted'

        return self.results

    def create_or_update_zone(self, zone):
        try:
            # create or update the new Zone object we created
            new_zone = self.private_dns_client.private_zones.create_or_update(
                self.resource_group, self.name, zone)

            if isinstance(new_zone, LROPoller):
                new_zone = self.get_poller_result(new_zone)

        except Exception as exc:
            self.fail("Error creating or updating zone {0} - {1}".format(
                self.name, exc.message or str(exc)))
        return zone_to_dict(new_zone)

    def delete_zone(self):
        try:
            # delete the Zone
            poller = self.private_dns_client.private_zones.delete(
                self.resource_group, self.name)
            result = self.get_poller_result(poller)
        except Exception as exc:
            self.fail("Error deleting zone {0} - {1}".format(
                self.name, exc.message or str(exc)))
        return result


def zone_to_dict(zone):
    # turn Zone object into a dictionary (serialization)
    result = dict(
        id=zone.id,
        name=zone.name,
        number_of_record_sets=zone.number_of_record_sets,
        number_of_virtual_network_links=zone.number_of_virtual_network_links,
        number_of_virtual_network_links_with_registration=zone.
        number_of_virtual_network_links_with_registration,
        tags=zone.tags)
    return result


def main():
    AzureRMPrivateDNSZone()


if __name__ == '__main__':
    main()
