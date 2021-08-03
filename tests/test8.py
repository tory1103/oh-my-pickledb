from src.my_pickledb import HopperDB

"""

Simple test to use HopperDB and its functions.
Functions used:
    .count_values() -> Counts the values and the times used
    .values_types() -> Creates a dictionary with all values and its types
    .count_values_types() -> Counts the types of values and the times used

Website: https://tory1103.github.io/oh-my-pickledb/
Documentation: https://tory1103.github.io/oh-my-pickledb/docs.html
Issues: https://github.com/tory1103/oh-my-pickledb/issues

"""

database = HopperDB("h.db", load=False)
database.set("my_example", "value0")
database.set("my_example2", "value0")
database.set("my_example3", "value1")
database.set("my_example4", "value2", "cva")

print(database.count_values())
print(database.values_types())
print(database.count_values_types())
