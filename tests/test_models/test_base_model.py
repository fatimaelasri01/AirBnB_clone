#!/usr/bin/python3
"""Defines the BaseModel class."""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Defines all common attributes/methods for other classes."""
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance."""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """Return a string representation of the BaseModel instance."""
        class_name = self.__class__.__name__
        self_id = self.id
        self_dict = self.__dict__
        return "[{}] ({}) {}".format(class_name, self_id, self_dict)

    def save(self):
        """Update the `updated_at` attribute with the current datetime."""
        self.updated_at = datetime.utcnow()
        storage.save()

    def to_dict(self):
        """Return a dictionary containing all keys/values of the instance."""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({"__class__": self.__class__.__name__})
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
