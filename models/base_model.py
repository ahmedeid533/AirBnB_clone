#!/usr/bin/python3
"""Defines a BaseModel class."""
import models
import uuid
from datetime import datetime


class BaseModel:
    """defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """init class"""
        self.created_at = datetime.today()
        self.id = str(uuid.uuid4())
        self.updated_at = datetime.today()
        timeformat = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(val, timeformat)
                else:
                    self.__dict__[key] = val
        else:
            models.storage.new(self)

    def __str__(self):
        """Creates the unofficial string representation
        of a BaseModel instance.
        Format: [<class name>] (<self.id>) <self.__dict__>
        Returns:
            The string representation of the object.
        """

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the updated_at attribute with the current_time."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Creates a dictionary containing all keys/values of __dict__ of the
        instance.
        A key __class__ is added to this dictionary with the class name of the
        object.
        Returns:
            Dictionary representations of the BaseModel instance.
        """
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['updated_at'] = dictionary['updated_at'].isoformat()
        dictionary['created_at'] = dictionary['created_at'].isoformat()
        return dictionary
