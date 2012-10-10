# -*- coding: utf-8 -*-
""" Viewlets """

from five import grok

from zope.interface import Interface
from zope.component import getUtility
from zope.annotation.interfaces import IAnnotations

from plone.app.layout.viewlets.interfaces import IAboveContent

from Products.CMFCore.interfaces import ISiteRoot


class AnnouncementViewlet(grok.Viewlet):
    """ Chat viewlet """

    grok.viewletmanager(IAboveContent)
    grok.context(Interface)
    grok.require("zope2.View")

    def update(self):
        site = getUtility(ISiteRoot)
        self.message = IAnnotations(site).get("pubsubannouncement", None)

