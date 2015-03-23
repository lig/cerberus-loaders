# Cerberus Loaders

[![Join the chat at https://gitter.im/lig/cerberus-loaders](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/lig/cerberus-loaders?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
Loaders to load [Cerberus](https://github.com/nicolaiarocci/cerberus) Validators from various data formats.

## Formats support
 * JSON
 * YaML
 * Python classes (planned)

## Usage

    from cerberus_loaders.json import validator_from_json
    
    v = validator_from_json(json_schema_file)
    v.validate({'field': 'value'})

## Python support
 * Python 2.7
 * Python 3.4
 * Python 3.5

Older versions could do the job too but are not supported.
