#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=line-too-long, undefined-variable, unused-argument, function-redefined

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import pexpect


@given(u'we have IWF installed')
def step_impl(context):
    pass


@given(u'we are operating "server00"')
def step_impl(context):
    pass


@when(
    u'we invoke the configure-ssl-security command with "--pfxFile" and values'
)
def step_impl(context):

    for row in context.table:
        pfx_file = row['pfx_file']
        cert_alias = row['cert_alias']
        cmd = 'ansible-playbook -i localhost, runbooks/configure_ssl_security.yml --extra-vars "download_file={} friendly_name={}"'.format(
            pfx_file, cert_alias)
        (output, status) = pexpect.run(cmd, withexitstatus=True, timeout=300)

    print(status)
    context.responses = output


@then(u'security.properties is updated')
def step_impl(context):
    pass


@then(u'the new certificate works')
def step_impl(context):
    pass
