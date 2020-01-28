"""This module contains boilerplate hashlib helpers."""
import hashlib

__all__ = ["md5", "sha1", "sha384", "sha3_384", "hash_any"]


def md5(obj):
    """Compute the MD5 of the given object."""
    if isinstance(obj, str):
        return hashlib.md5(obj.encode("utf-8")).hexdigest()
    return hashlib.md5(bytes(obj)).hexdigest()


def sha1(obj):
    """Compute the SHA1 of the given object."""
    if isinstance(obj, str):
        return hashlib.sha1(obj.encode("utf-8")).hexdigest()
    return hashlib.sha1(bytes(obj)).hexdigest()


def sha384(obj):
    """Compute the SHA384 of the given object."""
    if isinstance(obj, str):
        return hashlib.sha384(obj.encode("utf-8")).hexdigest()
    return hashlib.sha384(bytes(obj)).hexdigest()


def sha3_384(obj):
    """Compute the SHA3 384 of the given object."""
    if isinstance(obj, str):
        return hashlib.sha3_384(obj.encode("utf-8")).hexdigest()
    return hashlib.sha3_384(bytes(obj)).hexdigest()


def hash_any(obj, hasher):
    """ If hasher is a string, return the hash of the obj as specified by hasher. If hasher is an instance of hashlib's
     hashers, return the hash of the object from hasher. """
    if isinstance(obj, str):
        obj_bytes = obj.encode("utf-8")
    else:
        obj_bytes = bytes(obj)

    if isinstance(hasher, str):
        return hashlib.new(hasher, obj_bytes).hexdigest()
    elif str(type(hasher)) == "<class '_hashlib.HASH'>":
        hasher.update(obj_bytes)
        return hasher.hexdigest()
    else:
        raise TypeError("hasher is not a ??")
