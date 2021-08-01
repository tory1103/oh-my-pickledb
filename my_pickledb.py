import ast
import os
from collections import Counter

from cryptography.fernet import Fernet


class PickleDB:

    def __init__(self, location: str, load: bool = True, auto_dump: bool = False):
        """
        Creates a database object
        If load parameter is True, it will try to load the data from the location path
        If the file doesn´t exist, it will be created automatically

        If auto_dump parameter is True, it will try to save database after every update/query/change

        :param location:
        :param load:
        :param auto_dump:
        """

        self.location = location
        self.auto_save = auto_dump
        self.encrypt_token = bytes()

        self.database = dict()
        self.__update_database_type()

        if load: self.load()

        self.__setup_shortcuts()

    def __call__(self):
        """
        Returns current database

        :return: dict, str, bytes
        """
        return self.database

    def __getitem__(self, key: str):
        """
        Gets current value of the key in database

        :param key:
        :return: str
        """
        return self.get_value_by_key(key)

    def __setitem__(self, key: str, new_value):
        """
        Changes actual value of a key in database

        :param key:
        :param new_value:
        :return:
        """
        return self.create_key_and_value(key, new_value)

    def __delitem__(self, key: str):
        """
        Deletes current values and key in database

        :param key:
        :return:
        """
        return self.remove_value_by_key(key)

    def __update_database_type(self):
        """
        Updates database type:
            - Str
            - Dict
            - Bytes

        :return:
        """
        self.database_type = type(self.database)

    def __setup_shortcuts(self):
        """
        Creates functions shortcuts

        :return:
        """

        self.dump = self.save
        self.update = self.__update_database_type

        self.set = self.create_key_and_value
        self.get = self.get_value_by_key
        self.remove = self.remove_value_by_key

        self.getall_keys = lambda: list(self.database.keys())
        self.getall_items = lambda: list(self.database.items())
        self.getall_values = lambda: list(self.database.values())

    def load_as_str(self):
        """
        Loads database as string

        :return:
        """

        if os.path.exists(self.location):
            with open(self.location, "r") as database:
                self.database = database.read()
                self.__update_database_type()

        else:
            raise Exception("Database doesn´t exist")

        self.__update_database_type()
        return self.database

    def load_as_json(self):
        """
        Loads database as dictionary

        :return:
        """
        try:
            if os.path.exists(self.location):
                from json import load
                self.database = load(open(self.location, 'rt'))
                self.__update_database_type()

            else:
                raise Exception("Database doesn´t exist")

        except Exception as error:
            raise error

        self.__update_database_type()

    def load_as_bytes(self):
        """
        Loads database as bytes

        :return:
        """
        if os.path.exists(self.location):
            with open(self.location, "rb") as database:
                self.database = database.read()
                self.__update_database_type()

        else:
            raise Exception("Database doesn´t exist")

    def load(self):
        """
        Loads database automatically

        :return:
        """
        if not os.path.exists(self.location): return

        try:
            self.load_as_json()

        except:
            try:
                self.load_as_bytes()

            except:
                try:
                    self.load_as_str()

                except:
                    raise Exception("Unknown/Invalid database format")

        self.load_token()

    def save_as_str(self):
        """
        Saves database as string

        :return:
        """
        if self.database_type != str: self.convert_to_str()

        with open(self.location, "w") as database:
            database.write(self.database)

    def save_as_json(self):
        """
        Saves database as dictionary

        :return:
        """
        if self.database_type != dict: self.convert_to_json()

        from json import dump
        dump(self.database, open(self.location, 'wt'))

    def save_as_bytes(self):
        """
        Saves database as bytes

        :return:
        """
        if self.database_type != bytes: self.convert_to_bytes()

        with open(self.location, "wb") as database:
            database.write(self.database)

    def save(self, forcesave: bool = False):
        """
        Saves database automatically
        Forcesave parameter must be true to save it

        :param forcesave:
        :return:
        """
        if self.auto_save or forcesave:
            if self.database_type == dict:
                self.save_as_json()

            elif self.database_type == str:
                self.save_as_str()

            elif self.database_type == bytes:
                self.save_as_bytes()

            else:
                raise Exception("Unknown/Invalid database format")

    def convert_to_str(self):
        """
        Converts database to string format

        :return:
        """
        if self.database_type == dict:
            self.database = str(self.database)
            self.__update_database_type()

        if self.database_type == bytes:
            self.database = bytes.decode(self.database, "utf-8")
            self.__update_database_type()

    def convert_to_json(self):
        """
        Converts database to dictionary format

        :return:
        """
        if self.database_type == bytes:
            self.convert_to_str()

        if self.database_type == str:
            self.database = ast.literal_eval(self.database)
            self.__update_database_type()

    def convert_to_bytes(self):
        """
        Converts database to bytes format

        :return:
        """
        if self.database_type == dict: self.convert_to_str()

        if self.database_type == str:
            self.database = bytes(self.database, encoding="utf-8")
            self.__update_database_type()

    def create_key_and_value(self, key: str, *args):
        """
        Creates a new key and value on database

        :param key:
        :param args:
        :return:
        """
        self.database.update(
            {
                key: args[0] if len(args) == 1 else list(args)
            }
        )

        self.save()

    def get_value_by_key(self, key: str):
        """
        Gets database value by key

        :param key:
        :return:
        """
        return self.database.get(key)

    def remove_value_by_key(self, key: str):
        """
        Removes key and value by key on database

        :param key:
        :return:
        """

        value = self.database.pop(key)
        self.save()

        return value

    def search_keys_by_value(self, *args, accurate_search: bool = True):
        """
        Search for keys based on value
        If accurate_search value is True, it will search only for same values, if False, it will also add keys with the search_value on it
        It will return a list containing lists inside it with searched args

        Example:
            >>> database.search_keys_by_value("example_","exam")
            >>> [
                ['my_example_2', 'my_example_3'],
                ['my_example', 'my_example_2', 'my_example_3']
            ]

        :param accurate_search:
        :return:
        """

        find_values = lambda value: [key for key, val in self.database.items() if value == val or (value in val and not accurate_search)]
        return [find_values(value) for value in args]

    def search_keys_by_key(self, *args):
        """
        Search for keys if contained in args
        It will return a list containing lists inside it with searched args

        Example:
            >>> database.search_keys_by_key("example_", "exam")
            >>> [
                ['my_example_2', 'my_example_3'],
                ['my_example', 'my_example_2', 'my_example_3']
            ]

        :return: list
        """

        find_keys = lambda key: [k for k in self.database.keys() if key in k]
        return [find_keys(key) for key in args]

    def encrypt(self, use_token: bool = True, keep_type: bool = True):
        """
        Encrypts current database and returns its encoded value as bytes

        :param use_token: True if you want to use self.encrypted_token (saved)
        :param keep_type:
        :return: bytes
        """

        database_type = self.database_type if keep_type else None

        self.convert_to_bytes()

        self.encrypt_token = Fernet.generate_key() if not use_token or not self.encrypt_token else self.encrypt_token
        encryption = Fernet(self.encrypt_token).encrypt(self.database)

        self.convert_to_json() if database_type == dict else self.convert_to_str() if database_type == str else self.convert_to_bytes() if database_type == bytes else None
        return encryption

    def decrypt(self):
        """
        Decrypts current crypted database
        It converts database into json when decrypted

        :return:
        """

        if self.database_type != bytes: raise Exception("Database isn´t encrypted")
        if not self.encrypt_token: raise Exception("Must have encrypted token")

        self.database = Fernet(self.encrypt_token).decrypt(self.database)
        self.convert_to_json()

    def save_token(self):
        """
        Saves encrypt_token on file

        :return:
        """
        if self.encrypt_token:
            with open(f"{self.location}.token", "wb") as token: token.write(self.encrypt_token)

    def load_token(self):
        """
        Loads encrypt_token in file

        :return:
        """

        if not os.path.exists(self.location) or not os.path.exists(f"{self.location}.token"): return
        with open(f"{self.location}.token", "rb") as token: self.encrypt_token = token.read()

    def encrypt_and_save(self, save_token: bool = True, use_token: bool = True):
        """
        Save current database content on specified path with Fernet encoding
        It wont replace current database with the encoded one, it just save it encoded

        Example:
            >>> database = {"test":"test"}
            >>> ecncoded_database = gAAAAABhBBN8KLRLIMpu2MpE2GWgGm843Pb9fTfYiHx6ZjYg1ANLOMdDxShrProag_9F73Lf86KLFycxw6u_t-wrzhbTT19O7Q==

            >>> file.db >> gAAAAABhBBN8KLRLIMpu2MpE2GWgGm843Pb9fTfYiHx6ZjYg1ANLOMdDxShrProag_9F73Lf86KLFycxw6u_t-wrzhbTT19O7Q==

        Database still the same type and value

        :return:
        """

        self.database, self.encrypt_token = self.encrypt(use_token, False)
        self.save(True)

        if save_token: self.save_token()

    def decrypt_and_save(self):
        """
        Save current database content on specified path with Fernet decoding
        It wont replace current database with the encoded one, it just save it encoded

        Example:
            database = gAAAAABhBBN8KLRLIMpu2MpE2GWgGm843Pb9fTfYiHx6ZjYg1ANLOMdDxShrProag_9F73Lf86KLFycxw6u_t-wrzhbTT19O7Q==
            dencoded_database = {"test":"test"}

            file.db >> {"test":"test"}

        Database still the same type and value

        :return:
        """
        self.decrypt()
        self.save(True)


class HopperDB(PickleDB):
    def __init__(self, location: str, load: bool = True, auto_dump: bool = False):
        """
        Creates a database object with statistics method
        If load parameter is True, it will try to load the data from the location path
        If the file doesn´t exist, it will be created automatically

        If auto_dump parameter is True, it will try to save database after every update/query/change

        :param location:
        :param load:
        :param auto_dump:
        """
        super().__init__(location=location, load=load, auto_dump=auto_dump)

    def count_values(self):
        """
        Counts the values and the times used
        Returns a dictionary with the values and times

        If value type is 'unhashable type', it will be skipped

        Example:
            >>> pickledb.database = {"test": "1", "test2": "1", "test3": "2"}
            >>> pickledb.count_values()
            >>> {"1": 2, "2": 1}

        :return: dict
        """

        return dict(Counter([value for value in self.database.values() if type(value) == str]))

    def values_types(self):
        """
        Creates a dictionary with all values and its types

        Example:
            >>> pickledb.database = {"test": "1", "test2": ["1", "2"], "test3": {"2": "1"}}
            >>> pickledb.values_types()
            >>> {'test': <class 'str'>, 'test2': <class 'list'>, 'test3': <class 'dict'>}

        :return:
        """

        return {key: type(value) for key, value in self.database.items()}

    def count_values_types(self):
        """
        Counts the types of values and the times used
        Returns a dictionary with the types and times

        Example:
            >>> values = {'test': <class 'str'>, 'test2': <class 'str'>, 'test3': <class 'dict'>}
            >>> pickledb.count_values_types()
            >>> {<class 'str'>: 2 ,<class 'dict'>: 1}

        :return: dict
        """

        return dict(Counter(list(self.values_types().values())))
