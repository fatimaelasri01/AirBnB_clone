#!/usr/bin/python3
"""This module defines the BaseModel class."""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):

        tform = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    try:
                        setattr(self, k, datetime.strptime(v, tform))
                    except ValueError:
                        pass
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            storage.new(self)

    def save(self):
        """Update the 'updated_at' with the current datetime."""
        self.updated_at = datetime.today()
        from models import storage
        storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.
        Containing the key/value  __class__ representing
        the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """prints an instance of the object specified"""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
