#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test Config"""

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

from flaskr import create_app


def test_config():
    """Test create_app without passing test config."""
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing
