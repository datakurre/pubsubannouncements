# -*- coding: utf-8 -*-
import unittest2 as unittest

import re

from collective.zamqp.testing import runAsyncTest

from pubsubannouncements.testing import FUNCTIONAL_TESTING


class PubSubFunctional(unittest.TestCase):

    layer = FUNCTIONAL_TESTING

    def _testExchangeIsDeclared(self):
        rabbitctl = self.layer['rabbitctl']
        self.assertIn("announcements\tfanout",
                      rabbitctl('list_exchanges')[0].split("\n"))

    def testExchangeIsDeclared(self):
        runAsyncTest(self._testExchangeIsDeclared)

    def _testAnonymousQueueIsDeclared(self):
        rabbitctl = self.layer['rabbitctl']
        bindings = [re.sub("amq.gen-.*", "amq.gen-", binding) for binding
                    in rabbitctl('list_bindings')[0].split("\n")]
        self.assertIn("announcements\texchange\tamq.gen-", bindings)

    def testAnonymousQueueIsDeclared(self):
        runAsyncTest(self._testAnonymousQueueIsDeclared)

