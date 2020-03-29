#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function)
__metaclass__ = type

from collections import defaultdict
from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError
from ansible.utils.display import Display

DOCUMENTATION = """
        lookup: listmerge
        author: Jose Angel Munoz <josea.munoz@gmail.com>
        version_added: "2.9"
        short_description: merges lists from a given an array key
        description:
            - This lookup returns the contents of two or more merged lists using a common key.
        options:
          _terms:
            description: list(s) to merge
            required: True
        notes:
          - if key is not defined, "name" will be the default
          - use query if you want to return a list when a single value is given.
"""

display = Display()


class LookupModule(LookupBase):
    def run(self, terms, variables=None, **kwargs):

        array = defaultdict(dict)
        arraykey = "name"

        for items in terms:

            if isinstance(items, str):
                arraykey = items

            elif isinstance(items, list):
                for item in items:
                    try:
                        display.vvvv(u"Updating item %s" % item)
                        array[item[arraykey]].update(item)
                    except KeyError as exception:
                        raise AnsibleError("Key not found: %s" % exception)
            ret = list(array.values())

        return ret
