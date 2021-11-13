from cryptography.fernet import Fernet
from pysem_converters import isBytes, bytes_to_json, bytes_to_str

from .utils import Dictionary, Load, Save


class PickleDB(Dictionary):
    def __init__(self, file: str, **kwargs):
        """
        Creates a new PickleDB object
        File parameter is the path where you want to save pickledb dictionary

        :param file:
        :param kwargs:
        """

        super().__init__(**kwargs)
        self.save = self.dump = Save(file, self)

    def encrypt(self, token: bytes = None) -> bytes:
        """
        Encrypts current database and returns its encoded value as bytes
        Automatically saves encryption token on 'pickledb.token' file

        :param token:
        :return: bytes
        """

        encryption_token = Fernet.generate_key() if not token else token
        encryption = Fernet(encryption_token).encrypt(self.bytes)

        Save("token.pk", bytes_to_str(encryption_token)).as_str()

        return encryption

    def encrypt_and_save(self, file: str, token: bytes = None):
        """
        Saves current pickledb content on specified path with Fernet encoding

        Example:
            >>> database = {"test":"test"}
            >>> encoded_database = b'gAAAAABhBBN8KLRLIMpu2MpE2GWgGm843Pb9fTfYiHx6ZjYg1ANLOMdDxShrProag_9F73Lf86KLFycxw6u_t-wrzhbTT19O7Q=='

            << file.db >> b'gAAAAABhBBN8KLRLIMpu2MpE2GWgGm843Pb9fTfYiHx6ZjYg1ANLOMdDxShrProag_9F73Lf86KLFycxw6u_t-wrzhbTT19O7Q==''

        Database keeps the same type and value after enconding

        :param file:
        :param token:
        :return:
        """

        Save(file, bytes_to_str(self.encrypt(token))).as_str()


class LoadPickleDB(PickleDB):
    def __init__(self, file: str, **kwargs):
        """
        Creates a new PickleDB object
        File parameter is the path from where you want to load and save pickledb dictionary

        :param file:
        :param kwargs:
        """

        try: super().__init__(file, **Load(file).as_json(), **kwargs)
        except TypeError: raise Exception("Loaded object must be PickleDB or dictionary type")


class DecryptPickleDB(PickleDB):
    def __init__(self, file: str, token: Union[str, bytes], **kwargs):
        """
        Creates a new PickleDB object
        File parameter is the path from where you want to decrypt encrypted pickledb file object,
        it converts object into json when decrypted

        :param file:
        :param token:
        :param kwargs:
        """

        encryption = Load(file).as_bytes()
        encryption_token = token if isBytes(token) else Load(token).as_bytes()

        if not isBytes(encryption): raise Exception("PickleDB object isn´t encrypted")
        if not encryption_token: raise Exception("Must have encryption token")

        super().__init__(file, **bytes_to_json(Fernet(encryption_token).decrypt(encryption)), **kwargs)
