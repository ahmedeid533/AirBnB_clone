#!/usr/bin/python3
'''
This module defines FileStorage which is used to serializes and deserializes
instances to and fro json.
'''
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """vault for data"""

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        '''Initializes new FileStorage instance.'''
        return

    def all(self):
        '''
        Accessor of the class attribute __objects.

        Returns:
            The dictionary __objects.
        '''
        return FileStorage.__objects

    def new(self, obj):
        '''
        Enters obj into the __objects dictionary.

        Format: <obj class name>.id

        Args:
            obj : Object to be stored into the __objects dictionary.
        '''
        key = "{}.{}".format(obj.__class__.__name__, obj.id)

        FileStorage.__objects[key] = obj

    def save(self):
        '''
        Serializes the __objects dictionary into the json file
        (path: __file_path).
        '''
        opjects = FileStorage.__objects
        dictionary = {obj: opjects[obj].to_dict() for obj in opjects.keys()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(dictionary, file)

    def reload(self):
        '''
        Deserializes the stored instances from __file_path and reloads them
        as instances.
        '''
        try:
            with open(self.__file_path, "r") as file:
                dictionary = json.load(file)
                for opj in dictionary.values():
                    class_name = opj["__class__"]
                    del opj["__class__"]
                    self.new(eval(class_name)(**opj))
        except Exception:
            pass
