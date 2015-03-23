from __future__ import absolute_import  # py27

from json import load, loads

from cerberus import Validator


def validator_from_json(stream, **kwargs):
    """
    Load :class:`cerberus.Validator` schema from JSON file.

    :param stream: a stream object (string-like or file-like) containing a JSON
        document.
    """
    loader = hasattr(stream, 'read') and load or loads
    return Validator(loader(stream), **kwargs)
