from src.my_pickledb import PickleDB

"""

Simple test to use getall.
Functions used:
    .getall_keys -> Gets all saved keys
    .getall_items -> Gets all saved items
    .getall_values -> Gets all saved values

Website: https://tory1103.github.io/oh-my-pickledb/
Documentation: https://tory1103.github.io/oh-my-pickledb/docs.html
Issues: https://github.com/tory1103/oh-my-pickledb/issues

"""

database = PickleDB("my-example.db", load=False)
database.set("my_example", "value0")
database.set("my_example_2", "value0")
database.set("my_example_3", "value1")

print(database.getall_keys())
print(database.getall_items())
print(database.getall_values())
