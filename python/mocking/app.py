#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=import-outside-toplevel, undefined-variable

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

from datetime import datetime


def get_all_users():
    from db_connection import db
    results = db.query(Users).all()
    return results


def has_user_expired(user):
    if user.expiration_date < datetime.now():
        return True
    return False


def find_expired_users():
    expired_users = []
    users = get_all_users()
    for user in users:
        if has_user_expired(user):
            expired_users.append(user.id)
    return expired_users
