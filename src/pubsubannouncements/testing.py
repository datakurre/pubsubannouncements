# -*- coding: utf-8 -*-
""" Testing layers and keywords """

from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import FunctionalTesting

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
    bases=(PLONE_FIXTURE, z2.ZSERVER_FIXTURE),
    name="Acceptance")


class Keywords(object):
    """ Robot Framework keyword library """

    def get_site_owner_name(self):
        import plone.app.testing
        return plone.app.testing.interfaces.SITE_OWNER_NAME

    def get_site_owner_password(self):
        import plone.app.testing
        return plone.app.testing.interfaces.SITE_OWNER_PASSWORD
