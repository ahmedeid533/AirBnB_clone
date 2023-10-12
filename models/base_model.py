#!/usr/bin/python3
"""Defines a BaseModel class."""
import uuid
from datetime import datetime
import models


class BaseModel:
    """defines all common attributes/methods for other classes"""

    "you don't have to do Public instance attributes badr" 

    def __init__(self, *args, **kwargs):
        """init class"""
        self.created_at = datetime.today()
        self.id = str(uuid.uuid4())
        self.updated_at = datetime.today()
        timeformat = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, val in kwargs.items():
                    if key == "created_at" or key == "updated_at":
                        self.__dict__[key] = datetime.strptime(val, timeformat)
                    else:
                        self.__dict__[key] = val
        else:
            models.storage.new(self)
            
    "do Public instance methods here badr"
