from .pickledb import PickleDB


class FrameworkDBScheme(PickleDB):
    def __init__(self, location: str, load: bool = True, auto_dump: bool = False):
        super().__init__(location=location, load=load, auto_dump=auto_dump)

        if self.database_type != dict and self.encrypt_token: self.decrypt()

        self.current_id = max([self.database.get(key, 0).get("id", 0) for key in self.getall_keys()]) + 1 if load and len(self.getall_keys()) >= 1 and self.database_type == dict else 0

        self.setup_shortcuts()

    def get_current_id_and_sum(self):
        """
        Gets current saved id, and sums one when returned

        :return:
        """

        current = self.current_id
        self.current_id += 1
        return current

    def create_key_and_value(self, identifier: str, data: dict, expiration_time: int = None):
        """
        Creates a new key and value on database
        If expiration_time is setted, it will wait expiration time in seconds
        and then it will remove key from database

        It will automatically add an id

        Example:
            >>> database.set("identifier", {"test": "test"}, expiration_time=5)
            >>> print(database.database)
            >>> {"identifier": {"id": 0, "test": "test"}}

            # Sleeps 5 seconds and the removes it

            >>> print(database.database)
            >>> {}

        :param identifier:
        :param data:
        :param expiration_time:
        :return:
        """

        if type(data) != dict: raise Exception("Dictionary type needed")

        if not self.exists(identifier): self.database.update({identifier: {"id": self.get_current_id_and_sum(), **data}})
        else: self.database.update({identifier: {"id": self.database.get(identifier)["id"], **data}})

        if expiration_time:
            def remove_on_expiration( ):
                time.sleep(expiration_time)
                self.remove_value_by_key(identifier)

            threading.Thread(target=remove_on_expiration).start()

        self.save()

    def append_value_to_key(self, identifier: str, data: dict):
        """
        Appends *args to current saved key
        If key doesn´t exists, it will create it

        Example:
            >>> database.set("identifier", {"example_key": "test"})

            >>> database.append("identifier", {"example_key2": "test2"})
            >>> {"identifier": {"example_key": "test", "example_key2": "test2"}}


        :param identifier:
        :param data:
        :return:
        """

        self.create_key_and_value(identifier, {**self.get_value_by_key(identifier), **data}) if self.exists(identifier) else self.create_key_and_value(identifier, data)

    def search_by(self, by: str, where_is):
        """
        Searchs for all identifiers that contains 'by' key in its data,
        'by' key must be 'where_is' value

        It will return a list will all found identifiers

        Example:
            >>> database = Frameworks.UsersDB("my-example.db", load=False)

            >>> database.set("identifier0", {"example_key": "test"})
            >>> database.set("identifier1", {"example_key": "test1"})
            >>> database.set("identifier2", {"example_key": "test"})

            >>> print(database.search_by("example_key", "test"))
            >>> ['identifier0', 'identifier2']

        :param by:
        :param where_is:
        :return: list
        """

        return [x for x, y in self.database.items() if by in y and where_is == y[by]]


class UsersDB(FrameworkDBScheme):
    """
    This database is not meant to be used on production
    Its just a model/example to show how PickleDB can be used
    Create your own class instead
    """

    def __init__(self, location: str, load: bool = True, auto_dump: bool = False): super().__init__(location=location, load=load, auto_dump=auto_dump)

    def add_user(self, username: str, password: str, email: str, **options):
        """
        Creates a new user dictionary

        :param username:
        :param password:
        :param email:
        :param options:
        :return:
        """

        identifier = options.pop("identifier", f"id_{username}")
        self.create_key_and_value(
            identifier=identifier,
            data={
                "username": username,
                "password": password,
                "email": email,
                **options
            }
        )

        return identifier

    def remove_user(self, identifier: str):
        """
        Removes an user dictionary

        :param identifier:
        :return:
        """

        self.remove(identifier)


class ProductsDB(FrameworkDBScheme):
    """
    This database is not meant to be used on production
    Its just a model/example to show how PickleDB can be used
    Create your own class instead
    """

    def __init__(self, location: str, load: bool = True, auto_dump: bool = False): super().__init__(location=location, load=load, auto_dump=auto_dump)

    def add_product(self, product: str, price: str, **options):
        """
        Creates a new product dictionary

        :param product:
        :param price:
        :param options:
        :return:
        """

        identifier = options.pop("identifier", f"id_{product}")
        self.create_key_and_value(
            identifier=identifier,
            data={
                "product": product,
                "price": price,
                **options
            }
        )

        return identifier

    def remove_product(self, identifier: str):
        """
        Removes an product dictionary

        :param identifier:
        :return:
        """

        self.remove(identifier)
