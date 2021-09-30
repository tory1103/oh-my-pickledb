from src.my_pickledb import PickleDB

"""

Simple test to truncate a key
Functions used:
    .truncate() -> Removes key value but not key itself


Website: https://tory1103.github.io/oh-my-pickledb/
Documentation: https://tory1103.github.io/oh-my-pickledb/docs.html
Issues: https://github.com/tory1103/oh-my-pickledb/issues

"""

database = PickleDB("my-example.db")
database.set("my_example", "value0")

print(database.get("my_example"))
database.truncate("my_example")
print(database.get("my_example"))
