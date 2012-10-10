# -*- coding: utf-8 -*-
""" AMQP Producers """

from five import grok

from collective.zamqp.producer import Producer


class Announcer(Producer):
   grok.name("announcements")

   connection_id = "example"

   exchange = "announcements"
   exchange_type = "fanout"
   serializer = "text/plain"

   durable = False
