# -*- coding: utf-8 -*-
""" Testing layers and keywords """

from plone.app.testing import (
    PloneSandboxLayer,
    PLONE_FIXTURE,
    FunctionalTesting
)

from collective.zamqp.testing import (
    ZAMQP_FIXTURE,
    ZAMQP_ZSERVER_FIXTURE
)

from plone.testing import z2


class Layer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import pubsubannouncements
        self.loadZCML(package=pubsubannouncements)

FIXTURE = Layer()


FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE, ZAMQP_FIXTURE),
    name="Functional")

ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(FIXTURE, ZAMQP_ZSERVER_FIXTURE, z2.ZSERVER_FIXTURE),
    name="Acceptance")
