from __future__ import absolute_import  # py27

from json import load, loads

from cerberus import Validator


def validator_from_json(fp, **kwargs):
    """
    Load :class:`cerberus.Validator` schema from JSON file.

    :param fp: a ``.read()``-supporting file-like object containing a JSON
        document.
    """
    return Validator(load(fp, **kwargs))


def validator_from_jsons(s, **kwargs):
    """
    Load :class:`cerberus.Validator` schema from JSON string.

    :param s: a ``str`` instance containing a JSON document.
    """
    return Validator(loads(s, **kwargs))
