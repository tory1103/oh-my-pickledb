from src.my_pickledb import PickleDB

"""

Simple test to add, get and remove keys and values.
Functions used:
    .set() -> creates values
    .get() -> gets values
    .remove() -> deletes values

Website: https://tory1103.github.io/oh-my-pickledb/
Documentation: https://tory1103.github.io/oh-my-pickledb/docs.html
Issues: https://github.com/tory1103/oh-my-pickledb/issues

"""

database = PickleDB("my-example.db")
database.set("my_example", "value0")
print(database)

database.set("my_first_list", "value1", "value2", "value3")
print(database)

database.set("my_first_dictionary", {"example": "1"})
print(database)

"""

Also dictionary methods can be used as:
    database["my_example"]
    database["my_example"] = "example"
    del database["my_example"]
    
"""
