#!/usr/bin/env python3
"""Module for FileStorage class"""

import json
from models.user import User  # Import other models as needed

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, "w") as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                objs = json.load(f)
                for k, v in objs.items():
                    cls_name = k.split(".")[0]
                    if cls_name == "User":
                        self.__objects[k] = User(**v)
        except FileNotFoundError:
            pass
