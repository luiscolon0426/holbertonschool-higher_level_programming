#!/usr/bin/python3
""" module that test Rectangle"""

from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    """ class that test Rectangle class """

    @classmethod
    def setUpClass(cls):
        """ method that test the init class """
        cls.rect1 = Rectangle(5, 4)
        cls.rect2 = Rectangle(5, 4, 7)
        cls.rect3 = Rectangle(5, 4, 8, 9)

    def TestWidth(self):
        """ method that test width """
        self.assertEqual(self.rect1.width, 5)

    def test_height(self):
        """ method that test height """
        self.assertEqual(self.rect1.height, 4)

    def test_x(self):
        """ method that test x """
        self.assertEqual(self.rect1.height, 4)
        self.assertEqual(self.rect2.x, 7)

    def test_y(self):
        """ method that test y """
        self.assertEqual(self.rect1.height, 4)
        self.assertEqual(self.rect3.y, 9)

    def test_negative_x(self):
        """ method that test negative x"""
        self.assertEqual(self.rect1.height, 4)
        with self.assertRaises(ValueError) as cm:
            rectangle = Rectangle(6, 7, -9)

    def test_negative_y(self):
        """ method that test negative y """
        self.assertEqual(self.rect1.height, 4)
        with self.assertRaises(ValueError) as cm:
            rectangle = Rectangle(6, 7, 9, -9)

    def test_negative_width(self):
        """ method that test negative width """
        self.assertEqual(self.rect1.height, 4)
        with self.assertRaises(ValueError) as cm:
            rectangle = Rectangle(-4, 6)

    def test_negative_height(self):
        """ method that test negative height """
        self.assertEqual(self.rect1.height, 4)
        with self.assertRaises(ValueError) as cm:
            rectangle = Rectangle(4, -7)
