from cerberus_loaders.yaml import validator_from_yaml


def test_yaml(yaml_schema_file, validator):
    v = validator_from_yaml(yaml_schema_file)
    assert v.schema == validator.schema


def test_yamls(yaml_schema_string, validator):
    v = validator_from_yaml(yaml_schema_string)
    assert v.schema == validator.schema
