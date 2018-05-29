#!/usr/bin/env python3
# coding: utf-8

import unittest

import sys
sys.path.append('..')
from fooleng.tools.BSD.Stair import Stair

class TestStair(unittest.TestCase):
    def test_attrib(self):
        s = Stair(3, 2)
        self.assertEqual(s.L_0, 4.875)
        self.assertEqual(s.L, 5.724)
        self.assertEqual(s.h_1, 0.114)
        self.assertEqual(s.h_2, 0.068)
        self.assertEqual(s.h_3, 0.055)
        self.assertEqual(s.h, 0.237)
        self.assertEqual(s.areaStaticLoad, 7.110)
        self.assertEqual(s.areaLiveLoad, 3.5)
        self.assertEqual(s.lineStaticLoad, 20.349)
        self.assertEqual(s.lineLiveLoad, 20.034)

    def test_threeBoard(self):
        s = Stair(3, 3)
        self.assertEqual(s.L_0, 4.875)
        self.assertEqual(s.L, 5.724)
        self.assertEqual(s.h_1, 0.076)
        self.assertEqual(s.h_2, 0.068)
        self.assertEqual(s.h_3, 0.055)
        self.assertEqual(s.h, 0.199)
        self.assertEqual(s.areaStaticLoad, 5.970)
        self.assertEqual(s.areaLiveLoad, 4.9)
        self.assertEqual(s.lineStaticLoad, 20.349)
        self.assertEqual(s.lineLiveLoad, 30.051)

    def test_fourBoard(self):
        s = Stair(3, 4)
        self.assertEqual(s.L_0, 4.875)
        self.assertEqual(s.L, 5.724)
        self.assertEqual(s.h_1, 0.057)
        self.assertEqual(s.h_2, 0.068)
        self.assertEqual(s.h_3, 0.055)
        self.assertEqual(s.h, 0.180)
        self.assertEqual(s.areaStaticLoad, 5.400)
        self.assertEqual(s.areaLiveLoad, 7.0)
        self.assertEqual(s.lineStaticLoad, 20.349)
        self.assertEqual(s.lineLiveLoad, 40.068)
