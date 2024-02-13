#!/usr/bin/python3
"""This module defines the FileStorage class."""
from models.base_model import BaseModel
import json
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dict '__objects'."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in '__objects' 'obj' with key '<obj_class_name>.id'"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize '__objects' to the JSON file '__file_path'."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o.get("__class__", None)
                    if cls_name and '.' in cls_name:
                        module_name, class_name = cls_name.split('.')
                        module = getattr(models, module_name)
                        cls = getattr(module, class_name)
                        del o["__class__"]
                        self.new(cls(**o))
        except FileNotFoundError:
            pass
