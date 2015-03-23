from .json import validator_from_json
try:
    import yaml as _yaml
except ImportError:
    from warnings import warn
    warn('PyYAML is not installed YaML loader will not work')
else:
    from .yaml import validator_from_yaml
