"""This module contains boilerplate urllib helpers."""
import urllib

__all__ = ["update_qs"]


def update_qs(url, **kwargs):
    """Update a query string."""
    parts = list(urllib.parse.urlparse(url))
    queryargs = urllib.parse.parse_qs(parts[4], keep_blank_values=False)
    for k, v in kwargs.items():
        if v is None:
            del queryargs[k]
        else:
            queryargs[k] = v
    parts[4] = urllib.parse.urlencode(queryargs, doseq=True)
    return urllib.parse.urlunparse(parts)
