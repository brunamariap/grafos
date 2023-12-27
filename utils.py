import json


def read_json(path: str) -> dict:
    with open(path, 'r') as file:
        json_to_dict: dict = json.load(file)
        return json_to_dict


def key_converter(dictionary: dict) -> dict:
    new_dict = {int(external_key): {int(internal_key): value for internal_key,
                                    value in internal_dict.items()} for external_key, internal_dict in dictionary.items()}

    return new_dict
