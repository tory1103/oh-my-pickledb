from src.my_pickledb import DSLPickleDB

"""

Simple test to load DSL file.
Functions used:
    None

Website: https://tory1103.github.io/oh-my-pickledb/
Documentation: https://tory1103.github.io/oh-my-pickledb/docs.html
Issues: https://github.com/tory1103/oh-my-pickledb/issues

"""

database = DSLPickleDB("dsl_test.dsl")
print(database)
