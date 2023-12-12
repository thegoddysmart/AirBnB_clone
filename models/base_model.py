#!/usr/bin/python3
'''module for our base_model'''

import uuid
from datetime import datetime
import models

class BaseModel():
    '''For our class BaseModel'''
    def __init__(self, *args, **kwargs):
        '''For the class constructor of our class BaseModel'''
        if kwargs:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')

            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        '''updates to be 'updated_at' instance for current datetime'''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''dictionary rep. of our instance'''
        new_dict = dict(self.__dict__)
        new_dict['created_at'] = self.__dict__['created_at'].isoformat()
        new_dict['updated_at'] = self.__dict__['updated_at'].isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return (new_dict)

    def __str__(self):
        '''string of BaseModel instance'''
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

