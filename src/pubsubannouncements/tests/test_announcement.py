# -*- coding: utf-8 -*-
"""Functional testing using plone.app.testing"""

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

    def testViewletIsNotRendered(self):
        from zope.component import getMultiAdapter
        from Products.Five.browser import BrowserView
        from plone.app.layout.viewlets.interfaces import IAboveContent

        context = self.layer["portal"]
        request = self.layer["request"]
        view = BrowserView(context, request)

        abovecontent = getMultiAdapter((context, request, view), IAboveContent,
                                       name="plone.abovecontent")
        abovecontent.update()
        self.assertNotIn("Announcement", abovecontent.render())

    def _testViewletIsRendered(self):
        from zope.component import getMultiAdapter
        from Products.Five.browser import BrowserView
        from plone.app.layout.viewlets.interfaces import IAboveContent

        context = self.layer["portal"]
        request = self.layer["request"]

        view = BrowserView(context, request)

        abovecontent = getMultiAdapter((context, request, view), IAboveContent,
                                       name="plone.abovecontent")
        abovecontent.update()
        self.assertIn("Announcement", abovecontent.render())

    def testViewletIsRendered(self):
        context = self.layer["portal"]
        request = self.layer["request"]

        from zope.interface import alsoProvides
        from z3c.form.interfaces import IFormLayer
        alsoProvides(request, IFormLayer)

        from pubsubannouncements.forms import AnnouncementForm
        form = AnnouncementForm(context, request)
        request.form = {
            "form.widgets.message": "This is a test announcement!",
            "form.buttons.send": "Send",
        }
        form.update()

        runAsyncTest(self._testAnonymousQueueIsDeclared)

        import transaction
        transaction.commit()

        runAsyncTest(self._testViewletIsRendered)
