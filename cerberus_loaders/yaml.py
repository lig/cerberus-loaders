from __future__ import absolute_import  # py27

from yaml import load

from cerberus import Validator


def validator_from_yaml(stream, **kwargs):
    """
    Load :class:`cerberus.Validator` schema from YaML file.

    :param stream: a stream object (string-like or file-like) containing a YaML
        document.
    """
    return Validator(load(stream, **kwargs))
