from utils import access_nested_map

people = {"1": {'name': 'John', 'age': '27', 'sex': 'Male', "kids" : {"1": "John", "2": "Doe"}},
          "2": {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

nested_map = {"a": {"b": 2}}

result = access_nested_map(nested_map, "a")

print(result)