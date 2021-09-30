from src.my_pickledb import PickleDB

"""

Simple test to get value type
Functions used:
    .type() -> Gets value type by key


Website: https://tory1103.github.io/oh-my-pickledb/
Documentation: https://tory1103.github.io/oh-my-pickledb/docs.html
Issues: https://github.com/tory1103/oh-my-pickledb/issues

"""

database = PickleDB("my-example.db")
database.set("my_example", "value0")
database.set("my_example2", ["value0"])
database.set("my_example3", {"value1": "1"})

print(database.type("my_example"))
print(database.type("my_example2"))
print(database.type("my_example3"))
