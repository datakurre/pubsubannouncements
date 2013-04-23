# -*- coding: utf-8 -*-
from plone.testing import Layer
from plone.app.testing import PLONE_FIXTURE
from collective.zamqp.testing import RABBIT_FIXTURE


class RabbitPloneLayer(Layer):
    """An intermedia layer for robot-server to support RabbitMQ-layers
    with reload.

    Usage::
        bin/robot-server pubsubannouncements.testing.ACCEPTANCE_TESTING
            -l pubsubannouncements.testing_rabbitmq.RABBIT_PLONE_FIXTURE
    """
    defaultBases = (RABBIT_FIXTURE, PLONE_FIXTURE)

RABBIT_PLONE_FIXTURE = RabbitPloneLayer()
