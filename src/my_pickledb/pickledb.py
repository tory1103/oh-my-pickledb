import ast
import collections
import os
import threading
import time

from cryptography.fernet import Fernet

from .datatypes import isDictionary, isBytes, isString
from .helpers import convert_json_to_xml


class PickleDB:
    def __init__(self, location: str, load: bool = True, auto_save: bool = False, **kwargs):
        """
        Creates a database object
        If load parameter is True, it will try to load the data from the location path
        If the file doesn´t exist, it will be created automatically

        If auto_save parameter is True, it will try to save database after every update/query/change

        :param location:
        :param load:
        :param auto_save:
        """

        self.location = location
        self.auto_save = auto_save
        self.database = kwargs.get("database", {})
        if load and not self.database: self.load()

        self.encrypt_token = bytes()

        self.dump = self.save
        self.set = self.create_key_and_value
        self.append = self.append_value_to_key
        self.get = self.get_value_by_key
        self.remove = self.remove_value_by_key
        self.truncate = self.truncate_key
        self.exists = lambda key: key in self.database
        self.type = self.get_value_type_by_key

        self.getall_keys = lambda: list(self.database.keys())
        self.getall_items = lambda: list(self.database.items())
        self.getall_values = lambda: list(self.database.values())

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

    def load_as_str(self):
        """
        Loads database as string

        :return:
        """

        if not os.path.exists(self.location): raise Exception("Database doesn´t exist")

        with open(self.location, "r") as database: self.database = database.read()

    def load_as_json(self):
        """
        Loads database as dictionary

        :return:
        """

        if not os.path.exists(self.location): raise Exception("Database doesn´t exist")

        try:
            from json import load

            self.database = load(open(self.location, 'rt'))

        except Exception as error: raise error

    def load_as_bytes(self):
        """
        Loads database as bytes

        :return:
        """

        if not os.path.exists(self.location): raise Exception("Database doesn´t exist")

        with open(self.location, "rb") as database: self.database = database.read()

    def load(self):
        """
        Loads database automatically

        :return:
        """

        if not os.path.exists(self.location): raise Exception("Database doesn´t exist")

        try: self.load_as_json()
        except:
            try: self.load_as_bytes()
            except:
                try: self.load_as_str()
                except: raise Exception("Unknown/Invalid database format")

        self.load_token()

    def save_as_str(self):
        """
        Saves database as string

        :return:
        """

        if not isString(self.database): self.convert_to_str()

        with open(self.location, "w") as database: database.write(self.database)

    def save_as_json(self):
        """
        Saves database as dictionary

        :return:
        """

        if not isDictionary(self.database): self.convert_to_json()

        from json import dump

        dump(self.database, open(self.location, 'wt'))

    def save_as_bytes(self):
        """
        Saves database as bytes

        :return:
        """

        if not isBytes(self.database): self.convert_to_bytes()

        with open(self.location, "wb") as database: database.write(self.database)

    def save(self, forcesave: bool = False):
        """
        Saves database automatically
        Forcesave parameter must be true to save it

        :param forcesave:
        :return:
        """

        if self.auto_save or forcesave:
            if isDictionary(self.database): self.save_as_json()

            elif isString(self.database): self.save_as_str()

            elif isBytes(self.database): self.save_as_bytes()

            else: raise Exception("Unknown/Invalid database format")

    def export_as_xml(self, export_location: str):
        """
        Exports current database as XML Format

        :param export_location:
        :return:
        """

        self.convert_to_json()
        with open(export_location, "w") as xml: xml.write(convert_json_to_xml(self.database))

    def convert_to_str(self):
        """
        Converts database to string format

        :return:
        """

        self.database = str(self.database) if isDictionary(self.database) else bytes.decode(self.database, "utf-8") if isBytes(self.database) else self.database

    def convert_to_json(self):
        """
        Converts database to dictionary format

        :return:
        """

        if isBytes(self.database): self.convert_to_str()

        if isString(self.database): self.database = ast.literal_eval(self.database)

    def convert_to_bytes(self):
        """
        Converts database to bytes format

        :return:
        """

        if isDictionary(self.database): self.convert_to_str()

        if isString(self.database): self.database = bytes(self.database, encoding="utf-8")

    def create_key_and_value(self, key: str, *args, expiration_time: int = None):
        """
        Creates a new key and value on database
        If expiration_time is setted, it will wait expiration time in seconds
        and then it will remove key from database

        Example:
            >>> database = PickleDB("db.json")
            >>> database.set("test", "value", expiration_time=5)
            >>> print(database.database)
            >>> {"test": "value"}

            # Sleeps 5 seconds and the removes it

            >>> print(database.database)
            >>> {}

        :param key:
        :param args:
        :param expiration_time:
        :return:
        """

        self.database.update({key: args[0] if len(args) == 1 else [*args] if type(args[0]) != list else [*args[0], *args[1:]]})

        if expiration_time:
            def remove_on_expiration( ):
                time.sleep(expiration_time)
                self.remove_value_by_key(key)

            threading.Thread(target=remove_on_expiration).start()

        self.save()

    def append_value_to_key(self, key: str, *args):
        """
        Appends *args to current saved key
        If key doesn´t exists, it will create it

        Example:
            >>> database = PickleDB("db.json")
            >>> database.set("my_example", "value0")
            >>> 'value0'

            >>> database.append("my_example", "test")
            >>> ['value0', 'test']


        :param key:
        :param args:
        :return:
        """

        self.create_key_and_value(key, self.get_value_by_key(key), *args) if self.exists(key) else self.create_key_and_value(key, *args)

        self.save()

    def get_value_by_key(self, key: str, default_value: str = None):
        """
        Gets database value by key
        Default_value is returned if key doesnt exists

        :param key:
        :param default_value:
        :return:
        """

        return self.database.get(key, default_value)

    def get_value_type_by_key(self, key: str):
        """
        Gets database value by key
        Default_value is returned if key doesnt exists

        :param key:
        :return:
        """

        return type(self.get(key))

    def remove_value_by_key(self, key: str):
        """
        Removes key and value by key on database

        :param key:
        :return:
        """

        r = self.database.pop(key)
        self.save()
        return r

    def truncate_key(self, key: str):
        """
        Truncates a key value, this means, it removes key value but not key itself

        :param key:
        :return:
        """

        if self.exists(key): self.set(key, None)
        self.save()

    def search_keys_by_value(self, *args, accurate_search: bool = True):
        """
        Search for keys based on value
        If accurate_search value is True, it will search only for same values, if False, it will also add keys with the search_value on it
        It will return a list containing lists inside it with searched args

        Example:
            >>> database = PickleDB("db.json")
            >>> database.search_keys_by_value("example_","exam")
            >>> [
                ['my_example_2', 'my_example_3'],
                ['my_example', 'my_example_2', 'my_example_3']
            ]

        :param accurate_search:
        :return:
        """

        return [(lambda value: [key for key, val in self.database.items() if value == val or (value in val and not accurate_search)])(value) for value in args]

    def search_keys_by_key(self, *args):
        """
        Search for keys if contained in args
        It will return a list containing lists inside it with searched args

        Example:
            >>> database = PickleDB("db.json")
            >>> database.search_keys_by_key("example_", "exam")
            >>> [
                ['my_example_2', 'my_example_3'],
                ['my_example', 'my_example_2', 'my_example_3']
            ]

        :return: list
        """

        return [(lambda key: [k for k in self.database.keys() if key in k])(key) for key in args]

    def encrypt(self, use_token: bool = True, keep_type: bool = True):
        """
        Encrypts current database and returns its encoded value as bytes

        :param use_token: True if you want to use self.encrypted_token (saved)
        :param keep_type:
        :return: bytes
        """

        database_type = type(self.database) if keep_type else None

        self.convert_to_bytes()

        self.encrypt_token = Fernet.generate_key() if not use_token or not self.encrypt_token else self.encrypt_token
        encryption = Fernet(self.encrypt_token).encrypt(self.database)

        self.convert_to_json() if isDictionary(database_type) else self.convert_to_str() if isString(database_type) else self.convert_to_bytes() if isBytes(database_type) else None
        return encryption

    def encrypt_and_save(self, save_token: bool = True, use_token: bool = True):
        """
        Save current database content on specified path with Fernet encoding
        It wont replace current database with the encoded one, it just save it encoded

        Example:
            >>> database = {"test":"test"}
            >>> encoded_database = b'gAAAAABhBBN8KLRLIMpu2MpE2GWgGm843Pb9fTfYiHx6ZjYg1ANLOMdDxShrProag_9F73Lf86KLFycxw6u_t-wrzhbTT19O7Q=='

            << file.db >> b'gAAAAABhBBN8KLRLIMpu2MpE2GWgGm843Pb9fTfYiHx6ZjYg1ANLOMdDxShrProag_9F73Lf86KLFycxw6u_t-wrzhbTT19O7Q==''

        Database keeps the same type and value after enconding

        :return:
        """

        self.database = self.encrypt(use_token, False)
        self.save(True)

        if save_token: self.save_token()

    def decrypt(self):
        """
        Decrypts current crypted database
        It converts database into json when decrypted

        :return:
        """

        if not isBytes(self.database): raise Exception("Database isn´t encrypted")
        if not self.encrypt_token: raise Exception("Must have encrypted token")

        self.database = Fernet(self.encrypt_token).decrypt(self.database)
        self.convert_to_json()

    def decrypt_and_save(self):
        """
        Save current database content on specified path with Fernet decoding
        It wont replace current database with the encoded one, it just save it encoded

        Example:
            >>> database = b'gAAAAABhBBN8KLRLIMpu2MpE2GWgGm843Pb9fTfYiHx6ZjYg1ANLOMdDxShrProag_9F73Lf86KLFycxw6u_t-wrzhbTT19O7Q=='
            >>> decoded_database = {"test":"test"}

            << file.db >> {"test":"test"}

        Database is converted to json type

        :return:
        """

        self.decrypt()
        self.save(True)

    def load_token(self):
        """
        Loads encrypt_token in file

        :return:
        """

        if not os.path.exists(self.location) or not os.path.exists(f"{self.location}.token"): return
        with open(f"{self.location}.token", "rb") as token: self.encrypt_token = token.read()

    def save_token(self):
        """
        Saves encrypt_token on file

        :return:
        """

        if self.encrypt_token:
            with open(f"{self.location}.token", "wb") as token: token.write(self.encrypt_token)


class HopperDB(PickleDB):
    def __init__(self, location: str, load: bool = True, auto_dump: bool = False, **kwargs):
        """
        Creates a database object with statistics method
        If load parameter is True, it will try to load the data from the location path
        If the file doesn´t exist, it will be created automatically

        If auto_dump parameter is True, it will try to save database after every update/query/change

        :param location:
        :param load:
        :param auto_dump:
        """

        super().__init__(location=location, load=load, auto_dump=auto_dump, **kwargs)

    def count_values(self):
        """
        Counts the values and the times used
        Returns a dictionary with the values and times

        If value type is 'unhashable type', it will be skipped

        Example:
            >>> database = HopperDB("db.json", database={"test": "1", "test2": "1", "test3": "2"})
            >>> database.count_values()
            {"1": 2, "2": 1}

        :return: dict
        """

        return dict(collections.Counter([value for value in self.database.values() if type(value) == str]))

    def values_types(self):
        """
        Creates a dictionary with all values and its types

        Example:
            >>> database = HopperDB("db.json", database={"test": "1", "test2": ["1", "2"], "test3": {"2": "1"}})
            >>> database.values_types()
            {'test': <class 'str'>, 'test2': <class 'list'>, 'test3': <class 'dict'>}

        :return:
        """

        return {key: type(value) for key, value in self.database.items()}

    def count_values_types(self):
        """
        Counts the types of values and the times used
        Returns a dictionary with the types and times

        Example:
            >>> database = HopperDB("db.json", database={'test': <class 'str'>, 'test2': <class 'str'>, 'test3': <class 'dict'>})
            >>> database.count_values_types()
            {<class 'str'>: 2 ,<class 'dict'>: 1}

        :return: dict
        """

        return dict(collections.Counter(list(self.values_types().values())))
