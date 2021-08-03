from src.my_pickledb import PickleDB

"""

Simple test to use exists function and append.
Functions used:
    .append() -> Appends values to a key
    .exists() -> Determine if a key exists


Website: https://tory1103.github.io/oh-my-pickledb/
Documentation: https://tory1103.github.io/oh-my-pickledb/docs.html
Issues: https://github.com/tory1103/oh-my-pickledb/issues

"""

database = PickleDB("h.db", load=False)
database.set("my_example", "value0")
database.set("my_example2", "value0")
database.set("my_example3", "value1")
database.set("my_example4", "value2", "cva")

print(database.get("my_example"))
database.append("my_exampledfdfdf", "test")

assert database.exists("my_example")

print(database.get("my_example"))
print(database())
