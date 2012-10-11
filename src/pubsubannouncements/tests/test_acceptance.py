# -*- coding: utf-8 -*-
"""Acceptance testing using Robot Framework"""

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
