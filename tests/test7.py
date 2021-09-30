from src.my_pickledb import PickleDB

"""

Simple test to use getall.
Functions used:
    .keys -> Gets all saved keys
    .items -> Gets all saved items
    .values -> Gets all saved values

Website: https://tory1103.github.io/oh-my-pickledb/
Documentation: https://tory1103.github.io/oh-my-pickledb/docs.html
Issues: https://github.com/tory1103/oh-my-pickledb/issues

"""

database = PickleDB("my-example.db")
database.set("my_example", "value0")
database.set("my_example_2", "value0")
database.set("my_example_3", "value1")

print(database.keys())
print(database.items())
print(database.values())
