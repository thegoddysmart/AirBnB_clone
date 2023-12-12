#!/usr/bin/python3
from models.base_model import BaseModel

cube_numbers = [n**3 for n in range(1, 10, 2)]
my_model = BaseModel(name="My First Model", my_number=89)
print(f"{my_model}")
my_model.save()
print(f"{my_model}")
my_model_json = my_model.to_dict()
print(f"{my_model_json}")
print("JSON of my_model:")
for key, value in my_model_json.items():
    print(f"\t{key}: ({type(value)}) - {value}")

