from src.my_pickledb import DecryptPickleDB, Save

"""

Simple test to decrypt database.
Functions used:
    .set() -> creates values
    .decrypt() -> decrypt database using fernet encoding

Website: https://tory1103.github.io/oh-my-pickledb/
Documentation: https://tory1103.github.io/oh-my-pickledb/docs.html
Issues: https://github.com/tory1103/oh-my-pickledb/issues

"""

Save("my-example.encrypted", "gAAAAABhBEp8Rhx1h7ShXyIq_EUB-diHoGUJbIl5xvRfBWf7-Te1xDvbcBzc5-8VaVLMUxaetQkfwJeGs5_2SRCRtQ2iC3lGaCmaJzKba72sM1B8QoLBjAY=").as_str()
Save("my-example.token", "K3JN4iqw9yB4q1Ng3SF8y6aV0DlvP3vLKEXyZbkhqcA=").as_str()

database = DecryptPickleDB("my-example.encrypted", "my-example.token")
print(database)
