#!/usr/bin/python3
"""This is the class BaseModel"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:

    """defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """
        Initializes BaseModel instance.

        Args:
            - *args: list of arguments.
            - **kwargs: dictionary of key-values arguments.
        """

        if kwargs is not None and kwargs != {}:
            for value in kwargs:
                if value == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif value == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[value] = kwargs[value]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns official string representation"""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates updated_at attribute with current datetime"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns dictionary representation of BaseModel instance"""

        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = type(self).__name__
        obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()
        return obj_dict

