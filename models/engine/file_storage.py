#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json

from models.base_model import BaseModel

class FileStorage():
    """This class manages storage of hbnb models in JSON format"""
    __file_path = "file.json"
    __object = {}
    def all(self):
        return self.__object
    def new(self, obj):
        """Returns a dictionary of models currently in storage"""
        self.__object["{}.{}".format(type(obj).__name__, obj.id)] = obj
    def save(self):
        odict = {o: self.__object[0].to_dict() for o in self.__object.keys()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(odict, f)
    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(self.__file_path, "r", encoding="utf-8")  as f:
                for o in json.load(f).values():
                    name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(name)(**o))
        except FileNotFoundError:
            pass
