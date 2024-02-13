#!/usr/bin/python3
"""Tests for the BaseModel"""

import unittest
import datetime
import os
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Contains the actual tests"""

    def setUp(self):
        '''Set up the base by creating an instance of the BaseModel'''
        self.base_model = BaseModel()
        self.base_model1 = BaseModel()

    def tearDown(self):
        """Delete instances"""
        del self.base_model
        del self.base_model1

    def test_instances(self):
        """Tests if the instances are created"""
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertIsInstance(self.base_model1, BaseModel)

    def test_uuid(self):
        """Testing the uuid"""
        self.assertTrue(hasattr(self.base_model, "id"))
        self.assertTrue(hasattr(self.base_model1, "id"))
        self.assertNotEqual(self.base_model.id, self.base_model1.id)

    def test_datetime(self):
        """Test the created_at and update_at attributes"""
        self.assertTrue(hasattr(self.base_model, "created_at"))
        self.assertTrue(hasattr(self.base_model, "updated_at"))

        datenow = datetime.datetime.now()
        self.testmodel = BaseModel()
        self.assertNotEqual(self.testmodel.created_at, datenow)
        self.assertNotEqual(self.testmodel.created_at,
                            self.testmodel.updated_at)
        self.testmodel.save()
        self.assertNotEqual(self.testmodel.created_at,
                            self.testmodel.updated_at)

    def test_str(self):
        """Tests the __str__ method"""
        base_model = BaseModel()
        class_name = base_model.__class__.__name__
        dic = base_model.__dict__
        expected_output = "[{}] ({}) {}".format(class_name, base_model.id, dic)

        self.assertEqual(str(base_model), expected_output)

    def test_to_dict(self):
        """Tests the to_dict() method"""
        base_model = BaseModel()
        model_dict = base_model.to_dict()
        self.assertTrue(type(model_dict), dict)
        for key in model_dict:
            # check if the keys contain strings
            self.assertTrue(type(key), str)
            self.assertNotEqual(key, None)  # check if the keys are empty
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], base_model.id)
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_save_method(self):
        """Unittests for testing save method of the BaseModel class."""
        bm = BaseModel()
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)

        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())


if __name__ == '__main__':
    unittest.main()
