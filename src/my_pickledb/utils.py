from __future__ import annotations

from dataclasses import dataclass
from json import loads

from pysem_converters import isJson, isList, json_to_xml, str_to_json, str_to_bytes, Union


class Dictionary(dict):
    """
    PickleDB built-in mutable object

    Dictionary() -> New empty dictionary
    Dictionary(**kwargs) -> New dictionary initialized with the name=value pairs in the keyword argument list.
    For example:
        Dictionary(one=1, two=2) -> {"one": 1, "two": 2}
    """

    def __init__(self, **kwargs):
        """
        Creates a new custom dictionary object for PickleDB

        :param kwargs:
        """

        super().__init__(**kwargs)

    @property
    def str(self) -> str:
        """
        Converts self to string format

        :return:
        """

        return repr(self)

    @property
    def json(self) -> dict:
        """
        Converts self to json format

        :return:
        """

        return str_to_json(self.str)

    @property
    def bytes(self) -> bytes:
        """
        Converts self to bytes format

        :return:
        """

        return str_to_bytes(self.str)

    @property
    def xml(self) -> str:
        """
        Converts self to xml format

        :return:
        """

        return json_to_xml(self.json)

    def exists(self, key: str) -> bool: return key in self.json

    def set(self, key: str, *args, expiration_time: int = None) -> None:
        """
        Creates a new key and value on self dictionary
        If expiration_time is setted, it will wait expiration time in seconds
        and then it will remove key from self dictionary

        For example:
            >>> from my_pickledb import PickleDB
            >>> database = PickleDB("db.json")
            >>> database.set("test", "value", expiration_time=5)
            >>> print(database)
            >>> {"test": "value"}

            # Sleeps 5 seconds and the removes it

            >>> print(database)
            >>> {}

        :param key:
        :param args:
        :param expiration_time:
        :return:
        """

        self.update({key: args[0] if len(args) == 1 else [*args] if type(args[0]) != list else [*args[0], *args[1:]]})

        if expiration_time:
            from time import sleep
            from threading import Thread

            def remove_on_expiration( ):
                sleep(expiration_time)
                self.pop(key)

            Thread(target=remove_on_expiration).start()

    def append(self, key: str, *args, expiration_time: int = None) -> None:
        """
        Appends *args to current stored key
        If key doesn´t exists, it will create it

        For example:
            >>> from my_pickledb import PickleDB
            >>> database = PickleDB("db.json")
            >>> database.set("my_example", "value0")
            >>> 'value0'

            >>> database.append("my_example", "test")
            >>> ['value0', 'test']


        :param key:
        :param args:
        :param expiration_time:
        :return:
        """

        self.set(key, self.get(key), *args, expiration_time=expiration_time) if self.exists(key) else self.set(key, *args, expiration_time=expiration_time)

    def type(self, key: str) -> type:
        """
        Gets database value by key
        Default_value is returned if key doesnt exists

        :param key:
        :return:
        """

        return type(self.get(key))

    def truncate(self, key: str) -> None:
        """
        Truncates a key value, this means, it removes key value but not key itself

        :param key:
        :return:
        """

        if self.exists(key): self.set(key, None)

    def search_keys_by_value(self, *args, accurate_search: bool = True) -> list:
        """
        Search for keys based on value
        If accurate_search value is True, it will search only for same values, if False, it will also add keys with the search_value on it
        It will return a list containing lists inside it with searched args

        For example:
            >>> from my_pickledb import PickleDB
            >>> database = PickleDB("db.json")
            >>> database.search_keys_by_value("example_","exam")
            >>> [
                ['my_example_2', 'my_example_3'],
                ['my_example', 'my_example_2', 'my_example_3']
            ]

        :param accurate_search:
        :return:
        """

        return [(lambda value: [key for key, val in self.items() if value == val or (value in val and not accurate_search)])(value) for value in args]

    def search_keys_by_key(self, *args) -> list:
        """
        Search for keys if contained in args
        It will return a list containing lists inside it with searched args

        For example:
            >>> from my_pickledb import PickleDB
            >>> database = PickleDB("db.json")
            >>> database.search_keys_by_key("example_", "exam")
            >>> [
                ['my_example_2', 'my_example_3'],
                ['my_example', 'my_example_2', 'my_example_3']
            ]

        :return: list
        """

        return [(lambda key: [k for k in self.keys() if key in k])(key) for key in args]


class List(list):
    """
    PickleDB built-in mutable sequence object

    List() -> New empty list
    List(*args) -> New list initialized with the value singles in the args list.
    For example:
        List(1, 2) -> [1, 2]

    If no argument is given, the constructor creates a new empty list.
    """

    def __init__(self, *args):
        """
        Creates a new custom list object for PickleDB

        :param args:
        """

        super().__init__(args)

    @property
    def str(self) -> str:
        """
        Converts self to string format

        :return:
        """

        return repr(self)

    @property
    def json(self) -> list:
        """
        Converts self to json format

        :return:
        """

        return str_to_json(self.str)

    @property
    def bytes(self) -> bytes:
        """
        Converts self to bytes format

        :return:
        """

        return str_to_bytes(self.str)

    def merge(self, *args) -> None:
        """
        Merges current list with passed args lists
        It is an improved version of the .extend method
        Accepts multiple list arguments, not just one

        For example:
            >>> lst = List("test", "test2")
            >>> lst.merge(["my-example"], ["my-example2"])
            >>> print(lst)
            [ "test", "test2", "my-example", "my-example2" ]

        :param args:
        :return:
        """

        [self.extend(iterable) for iterable in args if isList(iterable)]

    def including(self, obj: Union[List, list, set, tuple]) -> Dictionary:
        """
        Converts current list and object passed list to Dictionary object
        It uses the zip method to convert to lists into an dictionary

        For example:
            >>> lst = List("test", "test2")
            >>> returned = lst.including(["my-example", "my-example2"])
            >>> print(returned)
            {'test': 'my-example', 'test2': 'my-example2'}

        :param obj:
        :return:
        """

        return Dictionary(**{x: y for x, y in zip(self, obj)})


class Save:
    """
    PickleDB built-in to save iterable objects
    """

    def __init__(self, file: str, obj: Union[Dictionary, List, dict, list, set, tuple]):
        """
        Saves self on custom file

        :param file:
        :param obj:
        :return:
        """

        self.__file = file
        self.__obj = obj

    def __call__(self, jsonify: bool = False, **kwargs) -> None: return self.as_str()

    def as_str(self) -> None:
        """
        Saves object as string on custom file

        :return:
        """

        with open(self.__file, "w") as f: f.write(str(self.__obj))

    def as_json(self) -> None:
        """
        Saves object as json on custom file

        :return:
        """

        from json import dump
        from ast import literal_eval

        obj = literal_eval(repr(self.__obj))
        if not isJson(obj): raise Exception("Json object is required")

        dump(obj, open(self.__file, 'wt'))

    def as_bytes(self) -> None:
        """
        Saves object as bytes on custom file

        :return:
        """

        with open(self.__file, "wb") as f: f.write(bytes(str(self.__obj), "utf-8"))

    def to_file(self, file: str) -> Save:
        """
        Changes saving file

        :param file:
        :return:
        """

        return Save(file, self.__obj)


class Load:
    """
    PickleDB built-in to load iterable objects
    """

    def __init__(self, file: str):
        """
        Loads a custom file

        :param file:
        :return:
        """

        self.__file = file

    def __call__(self, jsonify: bool = False, **kwargs) -> Union[str, bytes, dict, list, set, tuple]: return self.load(jsonify=jsonify, **kwargs)

    def as_str(self) -> str:
        """
        Loads objects as string of custom file

        :return:
        """

        return self.load()

    def as_json(self) -> Union[dict, list, set, tuple]:
        """
        Loads objects as json of custom file

        :return:
        """

        return self.load(jsonify=True)

    def as_bytes(self) -> bytes:
        """
        Loads objects as bytes of custom file

        :return:
        """

        return self.load(mode="rb")

    def load(self, jsonify: bool = False, **kwargs) -> Union[str, bytes, dict, list, set, tuple]:
        """
        Loads objects of a file
        If jsonify is True it will try to load it with json decoding
        otherwise it will load it as normal file

        :param jsonify:
        :param kwargs:
        :return:
        """

        with open(self.__file, kwargs.get("mode", "r")) as f: return str_to_json(f.read()) if jsonify else f.read()


def dsl_parser(data: str, separator: str = ":", arguments_separator: str = " "):
    @dataclass
    class dsl_t:
        type: str
        key: str
        value: Union[str, int, float, list, dict]

    try: arguments, value = data.split(separator)
    except: raise Exception(f"""Separator missing\n{data}\n{" " * data.find(separator)}^^^^""")

    try: value_type, key = arguments.strip().split(arguments_separator)
    except: raise Exception(f"""Value type or key missing\n{data}\n{" " * data.find(arguments)}^^^^""")

    value_type = value_type.lower()
    value = value.strip()

    try:
        if value_type in ["integer", "int", "i"]: value = int(value)

        elif value_type in ["float", "flt", "f"]: value = float(value)

        elif value_type in ["string", "str", "s"]: value = str(value)

        elif value_type in ["array", "arr", "a", "list", "l", "dictionary", "dict", "d", "json"]: value = loads(value)

        return dsl_t(type(value), key, value)

    except: raise Exception(f"""Type : {value_type} does not correspond with value""")
