#
# ex:ts=4:sw=4:sts=4:et
# -*- tab-width: 4; c-basic-offset: 4; indent-tabs-mode: nil -*-
#
# BitBake Toaster Implementation
#
# Copyright (C) 2016        Intel Corporation
#
# SPDX-License-Identifier: GPL-2.0-only
#

# Django settings for Toaster project.

# Settings overlay to use for running tests
# DJANGO_SETTINGS_MODULE=toastermain.settings-test

from toastermain.settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/toaster-test-db.sqlite',
        'TEST': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': '/tmp/toaster-test-db.sqlite',
        }
    }
}