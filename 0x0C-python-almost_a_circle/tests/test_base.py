#!/usr/bin/python3
""" unittest module for class """

from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    """ module for testing instantiation of the Base class """

    @classmethod
    def setUpClass(cls):
        """ setUp class method test """
        cls.b1 = Base()
        cls.b2 = Base()
        cls.b3 = Base()
        cls.b4 = Base(20)

    def test_id(self):
        """ method that test id """
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)

    def test_id_parameter(self):
        """ method that test id parameter """
        self.assertEqual(self.b4.id, 20)

    def test_increment(self):
        """ method that test increment """
        Base.__nb_objects = 0

        self.assertEqual(self.b1.id, 1)
