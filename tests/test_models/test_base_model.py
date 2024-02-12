#!/usr/bin/python3
"""Tests for the BaseModel."""

import unittest
import datetime
import os

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Contains the actual tests"""

    def setUp(self):
        """Set up the base by creating an instance of the BaseModel"""
        self.base_model = BaseModel()
        self.base_model1 = BaseModel()

    def tearDown(self):
        """Delete an instances"""
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
        """Test the created_at and update_at attributes:"""
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
        base_str = str(self.base_model)
        self.assertTrue(base_str.startswith("[BaseModel]"))
        self.assertTrue(base_str.endswith("}"))

    def test_todict(self):
        """Tests the to_dict() method:"""
        model_dict = self.base_model.to_dict()
        self.assertTrue(type(model_dict), dict)
        for key in model_dict:
            # check if the keys contain strings
            self.assertTrue(type(key), str)
            self.assertNotEqual(key, None)  # check if the keys are empty
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.base_model.id)
        self.assertEqual(model_dict['created_at'],
                         self.base_model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'],
                         self.base_model.updated_at.isoformat())

    def test_save(self):
        """Unittests for testing save method of the BaseModel class."""
        bm = BaseModel()
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)

        bm.save(None)  # test save with argument
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())

    def test_save_updates_file(self):
        """Check if calling save updates the file."""
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())

    def test_instance_attributes(self):
        """Check instance attributes."""
        base_model = BaseModel()
        self.assertIsInstance(base_model.id, str)
        self.assertIsInstance(base_model.created_at, datetime.datetime)
        self.assertIsInstance(base_model.updated_at, datetime.datetime)

        base_model_dict = base_model.to_dict()
        new_base_model = BaseModel(**base_model_dict)
        self.assertNotEqual(base_model, new_base_model)
        self.assertEqual(base_model.id, new_base_model.id)
        self.assertEqual(base_model.created_at, new_base_model.created_at)
        self.assertEqual(base_model.updated_at, new_base_model.updated_at)
        self.assertNotIn('__class__', new_base_model.__dict__)

    def test_str_method(self):
        """Check the __str__ method."""
        base_model = BaseModel()
        class_name = base_model.__class__.__name__
        dic = base_model.__dict__
        expected_output = "[{}] ({}) {}".format(class_name, base_model.id, dic)

        self.assertEqual(str(base_model), expected_output)

    def test_to_dict_method(self):
        """Check the to_dict method."""
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        new_created_at = base_model.created_at.isoformat()
        new_updated_at = base_model.updated_at.isoformat()

        self.assertIsInstance(base_model_dict, dict)
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertEqual(base_model_dict['id'], base_model.id)
        self.assertEqual(base_model_dict['created_at'], new_created_at)
        self.assertEqual(base_model_dict['updated_at'], new_updated_at)


if __name__ == '__main__':
    unittest.main()
