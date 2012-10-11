# -*- coding: utf-8 -*-
"""Acceptance testing using Robot Framework"""

###
# Monkeypatch http://bugs.python.org/issue14308 for Python 2.7.2
# to kill AttributeError noise due to a bug in threading._DummyThread
import threading


def __stop(self):
    # DummyThreads delete self.__block, but they have no waiters to
    # notify anyway (join() is forbidden on them).
    if not hasattr(self, '_Thread__block'):
        return
    self.__block.acquire()
    self.__stopped = True
    self.__block.notify_all()
    self.__block.release()
threading._DummyThread._Thread__stop = __stop
##

import unittest

from plone.testing import layered

from pubsubannouncements.testing import ACCEPTANCE_TESTING

import robotsuite


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(robotsuite.RobotTestSuite("test_announcement.txt"),
                layer=ACCEPTANCE_TESTING),
    ])
    return suite
