"""This module contains boilerplate hashlib helpers."""
import hashlib
from functools import singledispatch

__all__ = ["md5", "sha1", "sha384", "sha3_384", "hash_any"]


def md5(obj):
    """Compute the MD5 of the given object."""
    return hash_consumer(obj, hashlib.md5())


def sha1(obj):
    """Compute the SHA1 of the given object."""
    return hash_consumer(obj, hashlib.sha1())


def sha384(obj):
    """Compute the SHA384 of the given object."""
    return hash_consumer(obj, hashlib.sha384())


def sha3_384(obj):
    """Compute the SHA3 384 of the given object."""
    return hash_consumer(obj, hashlib.sha3_384())


def hash_any(obj, hasher):
    """ If hasher is a string, return the hash of the obj as specified by hasher. If hasher is an instance of hashlib's
     hashers, return the hash of the object from hasher. """

    if isinstance(hasher, str):
        hasher = hashlib.new(hasher)
    elif str(type(hasher)) != "<class '_hashlib.HASH'>":
        raise TypeError("hasher is not a ??")

    return hash_consumer(obj, hasher)


def hash_consumer(obj, hasher):
    """ Takes the given obj, and attempts to hash it using the hasher. """
    for hashable in any_to_hash(obj):
        hasher.update(bytes(hashable))
    return hasher.hexdigest()


@singledispatch
def any_to_hash(obj):
    for value in [a for a in dir(obj) if not callable(getattr(obj, a)) and not a.startswith("__")]:
        for item in any_to_hash(getattr(obj, value)):
            yield item

    try:
        obj_iter = iter(obj)
        for sub_obj in obj_iter:
            for item in any_to_hash(sub_obj):
                yield item
    except TypeError:
        pass


@any_to_hash.register(str)
def _any_to_hash_str(obj):
    yield obj.encode("utf-8")


@any_to_hash.register(int)
def _any_to_hash_int(obj):
    yield obj


@any_to_hash.register(bytes)
def _any_to_hash_bytes(obj):
    yield obj


@any_to_hash.register(bytearray)
def _any_to_hash_bytearray(obj):
    yield obj
