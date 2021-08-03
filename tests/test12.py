from time import sleep

from my_pickledb import PickleDB

"""

Simple test to expire keys.
Functions used:
    .set() -> creates values

Website: https://tory1103.github.io/oh-my-pickledb/
Documentation: https://tory1103.github.io/oh-my-pickledb/docs.html
Issues: https://github.com/tory1103/oh-my-pickledb/issues

"""

database = PickleDB("my-example.db", load=False)
database.set("my_example", "value0", expiration_time=2)
print(database())

sleep(3)
print(database())
