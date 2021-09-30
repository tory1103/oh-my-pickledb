import ast
from typing import Union


def isString(data) -> bool: return type(data) == str


def isInt(data) -> bool: return type(data) == int


def isFloat(data) -> bool: return type(data) == float


def isBytes(data) -> bool: return type(data) == bytes


def isBool(data) -> bool: return type(data) == bool


def isDictionary(data) -> bool: return type(data) == dict


def isList(data) -> bool: return type(data) == list


def isSet(data) -> bool: return type(data) == set


def isTuple(data) -> bool: return type(data) == tuple


def isJson(data) -> bool: return isDictionary(data) or isList(data) or isSet(data) or isTuple(data)


def json_to_str(json: Union[dict, list, set, tuple]) -> str: return str(json) if isJson(json) else json


def json_to_bytes(json: Union[dict, list, set, tuple]) -> bytes: return bytes(string, encoding="utf-8") if isString(string := json_to_str(json)) else string


def json_to_xml(json: dict) -> str: return "".join(["""<{tag}>{value}</{closetag}>""".format(tag=tag, value=json_to_xml(value) if isDictionary(value) else value, closetag=tag.split()[0]) for tag, value in json.items()]) if isDictionary(json) else json_to_str(json)


def str_to_bytes(string: str) -> bytes: return bytes(string, encoding="utf-8") if isString(string) else string


def str_to_json(string: str) -> Union[dict, list, set, tuple]: return ast.literal_eval(string) if isString(string) else string


def bytes_to_str(_bytes: bytes) -> str: return bytes.decode(_bytes, "utf-8") if isBytes(_bytes) else _bytes


def bytes_to_json(_bytes: bytes) -> Union[dict, list, set, tuple]: return str_to_json(bytes_to_str(_bytes)) if isBytes(_bytes) else _bytes
