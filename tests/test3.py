from my_pickledb import PickleDB

"""

Simple test to encrypt database.
Functions used:
    .set() -> creates values
    .encrypt() -> encrypts database using fernet encoding

Website: https://tory1103.github.io/oh-my-pickledb/
Documentation: https://tory1103.github.io/oh-my-pickledb/docs.html
Issues: https://github.com/tory1103/oh-my-pickledb/issues

"""

database = PickleDB("my-example.db", load=False)  # load = True; loads database automatically

database.set("my_example", "example")
database.database = database.encrypt(keep_type=False)
print(database.encrypt_token)
print(database(), database.database_type)  # Original Database
