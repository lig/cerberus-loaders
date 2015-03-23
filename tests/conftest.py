from pathlib import Path

from cerberus import Validator
import pytest


@pytest.fixture(scope='session')
def schema():
    return {
        'a_required_string': {
            'type': 'string',
            'minlength': 2,
            'maxlength': 10,
            'required': True,
        },
        'a_nullable_integer': {
            'type': 'integer',
            'nullable': True
        },
        'an_integer': {
            'type': 'integer',
            'min': 1,
            'max': 100,
        },
        'a_restricted_integer': {
            'type': 'integer',
            'allowed': [-1, 0, 1],
        },
        'a_boolean': {
            'type': 'boolean',
        },
        'a_datetime': {
            'type': 'datetime',
        },
        'a_float': {
            'type': 'float',
            'min': 1,
            'max': 100,
        },
        'a_number': {
            'type': 'number',
            'min': 1,
            'max': 100,
        },
        'a_set': {
            'type': 'set',
        },
        'a_regex_email': {
            'type': 'string',
            'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        },
        'a_readonly_string': {
            'type': 'string',
            'readonly': True,
        },
        'a_restricted_string': {
            'type': 'string',
            'allowed': ["agent", "client", "vendor"],
        },
        'an_array': {
            'type': 'list',
            'allowed': ["agent", "client", "vendor"],
        },
        'a_list_of_dicts_deprecated': {
            'type': 'list',
            'items': {
                    'sku': {'type': 'string'},
                    'price': {'type': 'integer'},
            },
        },
        'a_list_of_dicts': {
            'type': 'list',
            'schema': {
                    'type': 'dict',
                    'schema': {
                        'sku': {'type': 'string'},
                        'price': {'type': 'integer'},
                    },
            },
        },
        'a_list_of_values': {
            'type': 'list',
            'items': [{'type': 'string'}, {'type': 'integer'}, ]
        },
        'a_list_of_integers': {
            'type': 'list',
            'schema': {'type': 'integer'},
        },
        'a_dict': {
            'type': 'dict',
            'schema': {
                    'address': {'type': 'string'},
                    'city': {'type': 'string', 'required': True}
            },
        },
        'a_dict_with_keyschema': {
            'type': 'dict',
            'keyschema': {'type': 'integer'}
        },
        'a_list_length': {
            'type': 'list',
            'schema': {'type': 'integer'},
            'minlength': 2,
            'maxlength': 5,
        },
        'a_nullable_field_without_type': {
            'nullable': True
        },
        'a_not_nullable_field_without_type': {
        },
    }


@pytest.fixture(scope='session')
def validator(schema):
    return Validator(schema)


@pytest.fixture(scope='session')
def json_schema_filename():
    return str(
        Path(__file__).parent.joinpath('fixtures', 'schema.json').absolute())


@pytest.fixture()
def json_schema_file(json_schema_filename):
    return open(json_schema_filename)


@pytest.fixture()
def json_schema_string(json_schema_file):
    return json_schema_file.read()


@pytest.fixture(scope='session')
def yaml_schema_filename():
    return str(
        Path(__file__).parent.joinpath('fixtures', 'schema.yaml').absolute())


@pytest.fixture()
def yaml_schema_file(yaml_schema_filename):
    return open(yaml_schema_filename)


@pytest.fixture()
def yaml_schema_string(yaml_schema_file):
    return yaml_schema_file.read()
