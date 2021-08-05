from src.my_frameworks import UsersDB

"""

Simple test to use Frameworks.
Functions used:
    .add_user -> Creates an user dictionary
    .remove_user -> Removes an user dictionary

Website: https://tory1103.github.io/oh-my-pickledb/
Documentation: https://tory1103.github.io/oh-my-pickledb/docs.html
Issues: https://github.com/tory1103/oh-my-pickledb/issues

"""

database = UsersDB("my-example.db", load=False)
identifier = database.add_user("me", "1234", "test@test.com", moredata="here as keywords")
print(database())

database.remove_user(identifier)
print(database())
