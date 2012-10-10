# -*- coding: utf-8 -*-
"""Testing layers and keywords"""

from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import FunctionalTesting

from collective.zamqp.testing import ZAMQP_FIXTURE


class Layer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import pubsubannouncements
        self.loadZCML(package=pubsubannouncements)

FIXTURE = Layer()


FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE, ZAMQP_FIXTURE),
    name="Functional")
