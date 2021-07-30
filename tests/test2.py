from my_pickledb import PickleDB

"""

Simple test to load database from file.
Functions used:
    .load() -> loads database
    
Database must exists, else it will create one.

Website: https://tory1103.github.io/oh-my-pickledb/
Documentation: https://tory1103.github.io/oh-my-pickledb/docs.html
Issues: https://github.com/tory1103/oh-my-pickledb/issues

"""

database = PickleDB("my-example.db", load=False)  # load = True; loads database automatically

print(database())  # Before loading it
database.load()
print(database())  # After loading it
