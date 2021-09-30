from src.my_pickledb import PickleDB

"""

Simple test to add and save keys and values in file.
Functions used:
    .set() -> creates values
    .save() -> saves database

Website: https://tory1103.github.io/oh-my-pickledb/
Documentation: https://tory1103.github.io/oh-my-pickledb/docs.html
Issues: https://github.com/tory1103/oh-my-pickledb/issues

"""

database = PickleDB("my-example.db")

database.set("my_example", "value0")
database.save.as_json()
