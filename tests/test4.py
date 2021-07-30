from my_pickledb import PickleDB

"""

Simple test to decrypt database.
Functions used:
    .set() -> creates values
    .decrypt() -> decrypt database using fernet encoding

Website: https://tory1103.github.io/oh-my-pickledb/
Documentation: https://tory1103.github.io/oh-my-pickledb/docs.html
Issues: https://github.com/tory1103/oh-my-pickledb/issues

"""

database = PickleDB("my-example.db", load=False)  # load = True; loads database automatically

database.database = b"gAAAAABhBEp8Rhx1h7ShXyIq_EUB-diHoGUJbIl5xvRfBWf7-Te1xDvbcBzc5-8VaVLMUxaetQkfwJeGs5_2SRCRtQ2iC3lGaCmaJzKba72sM1B8QoLBjAY="
database.encrypt_token = b"K3JN4iqw9yB4q1Ng3SF8y6aV0DlvP3vLKEXyZbkhqcA="
database.update()

print(database())  # Original Database
database.decrypt()
print(database())

