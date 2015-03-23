from cerberus_loaders.json import validator_from_json, validator_from_jsons


def test_json(json_schema_file, validator):
    v = validator_from_json(json_schema_file)
    assert v.schema == validator.schema


def test_jsons(json_schema_file, json_schema_string, validator):
    v = validator_from_jsons(json_schema_string)
    assert v.schema == validator.schema
