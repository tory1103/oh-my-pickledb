from src.my_pickledb import LoadPickleDB

"""

Simple test to load database from file.
Class used:
    LoadPickleDB() -> loads database
    
Database must exists, else it will create one.

Website: https://tory1103.github.io/oh-my-pickledb/
Documentation: https://tory1103.github.io/oh-my-pickledb/docs.html
Issues: https://github.com/tory1103/oh-my-pickledb/issues

"""

database = LoadPickleDB("my-example.db")
print(database)  # Before loading it
