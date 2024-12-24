import datetime
from enum import Enum
from pathlib import Path
import inspect
import requests
import os
import json

TEST_DIR = os.path.dirname(__file__)

def download_if_required(path: str):
    """Downloads a file if not present in the filesystem"""
    # do nothing if file already exists
    if os.path.isfile(path):
        return

    # check if there exists a .ftp file to fetch the target file    
    file_path = Path(path)
    ftp_file_path = file_path.with_name(f'{os.path.splitext(file_path.name)[0]}.ftp')

    if not os.path.isfile(ftp_file_path):
        raise FileNotFoundError(f'Unable to find either file or download source for "{path}".')
    
    # read the .ftp file
    with open(ftp_file_path, 'r', encoding='utf-8') as f:
        url = f.read().replace('\n', '').strip()
    
    # try to download missing file
    result = requests.get(url)
    if result.status_code != 200:
        raise Exception(f'Unable to download "{path}" from "{url}".')
    
    with open(path, 'wb') as f:
        f.write(result.content)


def path_for(file: str) -> str:
    """Returns path to test data"""
    path = os.path.join(TEST_DIR, 'data', file)
    download_if_required(path)
    return path

def info_json_for(file: str) -> str:
    name = os.path.splitext(os.path.split(file)[-1])[0]
    return path_for(f'{name}.info.json')


def assert_attribute(actual, expected):
    """Asserts that the given attribute matches the expected value"""
    if type(expected) is dict:
        keys = expected.keys()
        if len(keys) == 2 and 'type' in keys and 'value' in keys:
            type_name = expected['type']
            assert type(actual).__name__ == type_name, f'Expected value to have "{type_name}" type'

            value = expected['value']
            if type_name == 'datetime':
                value = datetime.datetime.fromisoformat(value)
            elif isinstance(actual, Enum):
                actual = actual.value

            assert actual == value, f'Expected value to be "{value}"'
        else:
            for attribute_name, attribute_value in expected.items():
                assert hasattr(actual, attribute_name), f'Expected attribute "{attribute_name}"'
                assert_attribute(getattr(actual, attribute_name), attribute_value)
    elif type(expected) is list:
        assert type(actual) is list, 'Expected value to be list'
        assert len(actual) == len(expected), f'Expected list value to have length {len(expected)}'

        for expected_item, actual_item in zip(expected, actual):
            assert_attribute(actual_item, expected_item)
    elif type(expected) is float:
        assert type(actual) is float, f'Expected value to be float'
        assert abs(actual - expected) < 1e-9
    else:
        assert actual == expected, f'Expected value to be "{expected}"'

def assert_attributes(access, path: str):
    """Asserts object attributes against *.info.json file."""

    # load info json for .raw file
    info_json_path = info_json_for(access.file_name)

    if not os.path.isfile(info_json_path):
        raise FileNotFoundError(f'The info.json file "{info_json_path}" does not exist.')
    
    with open(info_json_path, 'r', encoding='utf-8') as f:
        info_json = json.load(f)

    # locate node of interest in info json
    path_parts = path.split('.') if '.' in path else [path]
    expected_node = info_json
    actual_node = access
    for attr in path_parts:
        expected_node = expected_node[attr]
        actual_node = getattr(actual_node, attr)

    assert_attribute(actual_node, expected_node)

def capture_attribute_as_dict(access, path: str):
    """Capture object attribute and output to dictionary"""
    
    # locate node of interest in info json
    path_parts = path.split('.') if '.' in path else [path]
    node = access
    for attr in path_parts:
        node = getattr(node, attr)
    
    # generate dictionary
    capture = dict()
    for attribute_name, attribute_value in inspect.getmembers(node):
        if attribute_name.startswith('_'):
            continue
        
        if type(attribute_value) is dict:
            capture[attribute_name] = capture_attribute_as_dict(attribute_value)
        elif type(attribute_value) is list:
            list_value = list()
            for item in attribute_value:
                if type(item) is dict:
                    list_value.append(capture_attribute_as_dict(item))
                else:
                    list_value.append(item)
            capture[attribute_name] = list_value
        elif isinstance(attribute_value, Enum):
            capture[attribute_name] = { 'type': type(attribute_value).__name__, 'value': attribute_value.value }
        elif type(attribute_value) is datetime.datetime:
            capture[attribute_name] = { 'type': 'datetime', 'value': str(attribute_value) }
        elif type(attribute_value).__name__ == 'method':
            continue
        else:
            capture[attribute_name] = attribute_value
    
    return capture

def capture_attribute(access, path: str):
    """Capture object attribute and output to console"""
    print(json.dumps(capture_attribute_as_dict(access, path), indent=4))
    