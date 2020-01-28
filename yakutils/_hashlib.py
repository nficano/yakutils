"""This module contains boilerplate hashlib helpers."""
import hashlib

__all__ = ["md5", "sha1", "sha384", "sha3_384"]


def md5(val):
    """Compute the MD5 of a given string."""
    return hashlib.md5(val.encode("utf-8")).hexdigest()


def sha1(val):
    """Compute the SHA-1 of a given string."""
    return hashlib.sha1(val.encode("utf-8")).hexdigest()


def sha384(val):
    """Compute the SHA-384 of a given string."""
    return hashlib.sha384(val.encode("utf-8")).hexdigest()


def sha3_384(val):
    """Compute the SHA3-384 of a given string."""
    return hashlib.sha3_384(val.encode("utf-8")).hexdigest()
