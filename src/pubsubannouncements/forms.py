# -*- coding: utf-8 -*-
""" Announcement Form """

from five import grok

from zope.component import getUtility
from zope.schema import Text

from plone.directives import form

from Products.CMFCore.interfaces import ISiteRoot
from Products.statusmessages.interfaces import IStatusMessage

from z3c.form import button

from collective.zamqp.interfaces import IProducer


class IAnnouncementForm(form.Schema):

    message = Text(
        title=u"Announcement message",
        description=(u"The message will be broadcasted to all subscribers. "
                     u"An empty message will clear the announcement."),
        required=False
    )


class AnnouncementForm(form.SchemaForm):

    grok.name("send-announcement")
    grok.require("cmf.ModifyPortalContent")
    grok.context(ISiteRoot)

    schema = IAnnouncementForm
    ignoreContext = True

    label = u"Announce"
    description = u"Or send an empty announcement to clear the previous one."

    def update(self):
        self.request.set("disable_border", True)
        super(AnnouncementForm, self).update()

    @button.buttonAndHandler(u"Send")
    def handleSend(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return

        producer = getUtility(IProducer, name="announcements")
        producer.register()
        producer.send(data.get("message", ""))

        IStatusMessage(self.request).addStatusMessage(u"Done.")
