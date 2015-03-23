from cerberus_loaders.json import validator_from_json


def test_json(json_schema_file, validator):
    v = validator_from_json(json_schema_file)
    assert v.schema == validator.schema
