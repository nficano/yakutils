"""This module contains boilerplate hashlib helpers."""
import hashlib

__all__ = ["md5", "sha1"]


def md5(s):
    """Compute the MD5 of a given string."""
    return hashlib.md5(s.encode("utf-8")).hexdigest()


def sha1(s):
    """Compute the SHA1 of a given string."""
    return hashlib.sha1(s.encode("utf-8")).hexdigest()
