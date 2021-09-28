def create_xml_element(tag: str, value, **kwargs):
    """
    Creates an XML Element ( <tag>value</tag> )

    :param tag:
    :param value:
    :return:
    """

    return f"""<{tag}>{value}</{kwargs.get("closetag", tag)}>"""


def convert_json_to_xml(dictionary: dict):
    """
    Converts json object to XML object
    It returns an string object with XML code

    :param dictionary:
    :return:
    """

    return "".join([create_xml_element(tag, convert_json_to_xml(value) if type(value) == dict else value, closetag=tag.split()[0]) for tag, value in dictionary.items()])


def convert_json_file_to_xml(file: str):
    """
    Converts json file object to XML object
    It returns an string object with XML code

    :param file:
    :return:
    """

    try:
        from json import load

        return convert_json_to_xml(load(open(file, 'rt')))

    except Exception as error: raise error
