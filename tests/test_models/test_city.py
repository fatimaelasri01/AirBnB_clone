#!/usr/bin/python3
"""Tests for the City model"""
import unittest
import datetime
from models.city import City
from models.base_model import BaseModel
import os


class TestBaseModel(unittest.TestCase):
    def test_instance_attributes(self):
        city = City()
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)


if __name__ == '__main__':
    unittest.main()
