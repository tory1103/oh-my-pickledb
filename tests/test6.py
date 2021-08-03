from src.my_pickledb import PickleDB

"""

Simple test to search keys in database.
Functions used:
    .set() -> creates values
    .search_keys() -> searchs for keys by value

Website: https://tory1103.github.io/oh-my-pickledb/
Documentation: https://tory1103.github.io/oh-my-pickledb/docs.html
Issues: https://github.com/tory1103/oh-my-pickledb/issues

"""

database = PickleDB("my-example.db", load=False)
database.set("my_example", "value0")
database.set("my_example_2", "value0")
database.set("my_example_3", "value1g")

print(database.search_keys_by_key("example_"))
