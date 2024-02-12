#!/usr/bin/python3
"""Tests for the State Model"""
import unittest
import datetime
from models.state import State
from models.base_model import BaseModel
import os


class TestBaseModel(unittest.TestCase):
    def test_instance_attributes(self):
        state = State()
        self.assertIsInstance(state.name, str)


if __name__ == '__main__':
    unittest.main()
