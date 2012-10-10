# -*- coding: utf-8 -*-
""" AMQP Consumers """

from five import grok

from zope.component import getUtility
from zope.annotation.interfaces import IAnnotations

from Products.CMFCore.interfaces import ISiteRoot

from collective.zamqp.consumer import Consumer
from collective.zamqp.interfaces import IMessageArrivedEvent

from pubsubannouncements.interfaces import IAnnouncement


class Announcements(Consumer):
    grok.name("announcements")

    connection_id = "example"

    exchange = "announcements"
    exchange_type = "fanout"
    queue = ""  # anonymous queue
    durable = False

    marker = IAnnouncement


@grok.subscribe(IAnnouncement, IMessageArrivedEvent)
def handleMessage(message, event):
    site = getUtility(ISiteRoot)
    IAnnotations(site)["pubsubannouncement"] = message.body
    message.ack()
