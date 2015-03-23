# Cerberus Loaders
Loaders to load [Cerberus](https://github.com/nicolaiarocci/cerberus) Validators from various data formats.

## Formats support
 * JSON
 * YaML (planned)
 * Python classes (planned)

## Usage

    from cerberus_loaders.json import validator_from_json
    
    v = validator_from_json(json_schema_file)
    v.validate({'field': 'value'})
