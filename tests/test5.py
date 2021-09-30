from src.my_pickledb import PickleDB

"""

Simple test to search values in database.
Functions used:
    .set() -> creates values
    .search_value() -> searchs for keys by value

Website: https://tory1103.github.io/oh-my-pickledb/
Documentation: https://tory1103.github.io/oh-my-pickledb/docs.html
Issues: https://github.com/tory1103/oh-my-pickledb/issues

"""

database = PickleDB("my-example.db")
database.set("my_example", "value0")
database.set("my_example_2", "value0")
database.set("my_example_3", "value1")

print(database.search_keys_by_value("value0", "1", accurate_search=False))
