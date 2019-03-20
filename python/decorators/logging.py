#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Loggin"""

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

from functools import wraps


def loggit(func):
    """ Loggit Decorator """

    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return with_logging


def logit(logfile='out.log'):
    """ Logit Decorator """

    def logging_decotator(func):
        @wraps(func)
        def wrapped_function():
            log_string = func.__name__ + " was called"
            print(log_string)
            # Open the logfile and append
            with open(logfile, 'a') as opened_file:
                # Now we log to the specified logfile
                opened_file.write(log_string + '\n')

        return wrapped_function

    return logging_decotator


@loggit
def addition_func(number):
    """ Do some math """
    return number + number


RESULT = addition_func(4)
print(RESULT)


@logit()
def myfunc1():
    """ MyFunc1 """


myfunc1()


@logit(logfile='func2.log')
def myfunc2():
    """ MyFunc2 """


myfunc2()


class LoggitClass:
    """ Logit Class """

    _logfile = 'out.log'

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        log_string = self.func.__name__ + " was called"
        print(log_string)
        # Open the logfile and append
        with open(self._logfile, 'a') as opened_file:
            # Now we log to the specified logfile
            opened_file.write(log_string + '\n')
        # Now, send a notification
        self.notify()

        # return base func
        return self.func(*args)

    def notify(self):
        """ logit only logs, no more """


class EmailLogit(LoggitClass):
    """
    A logit implementation for sending emails to admins
    when the function is called.
    """

    def __init__(self, email, *args, **kwargs):
        self.email = email
        super(EmailLogit, self).__init__(*args, **kwargs)

    def notify(self):
        """ logit only logs, no more """

    def anothermethod(self):
        """ Another Method """


@LoggitClass
def myfunc3():
    """ MyFunc2 """


myfunc3()
