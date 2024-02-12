#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py."""
import unittest
import os
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class FileStorageTestCase(unittest.TestCase):
    def setUp(self):
        """Clears the content of the __objects first."""
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """Deletes the file to ensure a clean slate."""
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_obj_list_empty(self):
        """Ensures that the __objects is empty at the start."""
        self.assertEqual(len(storage.all()), 0)

    def test_filestorage_instance(self):
        """Checks that storage is correctly instantiated."""
        self.assertIsInstance(storage, FileStorage)
        base_model = BaseModel()
        base_model.save()
        all_objects = storage.all()
        self.assertEqual(len(all_objects), 1)
        self.assertIn("BaseModel.{}".format(base_model.id), all_objects)

    def test_new_method(self):
        """Checks that the new instance is added to the __objects."""
        base_model = BaseModel()
        for obj in storage._FileStorage__objects.values():
            self.assertEqual(obj, base_model)

    def test_save_method(self):
        """Tests that it saves in a `file.json`."""
        base_model = BaseModel()
        base_model.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload_no_file(self):
        """Tests that the instance is reinitialized."""
        bm = BaseModel()
        storage.new(bm)
        storage.save()
        storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)

    def test_reload_empty(self):
        """Load from an empty file."""
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """Nothing happens if file does not exist."""
        self.assertEqual(storage.reload(), None)


if __name__ == '__main__':
    unittest.main()
