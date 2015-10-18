#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest

from pynodebb import Client
from pynodebb.settings import settings


class TestPyNodeBBHttpClient(unittest.TestCase):
    def test_should_set_default_admin_uid(self):
        client = Client('http://localhost:4567', 'master_tokenxxx')
        self.assertEquals(client.http_client.admin_uid, settings['admin_uid'])

    def test_should_set_bearer_headers(self):
        client = Client('http://localhost:4567', 'master_tokenxxx')
        self.assertEquals(client.http_client.headers, {
            'Authorization': 'Bearer %s' % 'master_tokenxxx'
        })
