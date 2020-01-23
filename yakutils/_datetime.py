"""This module contains boilerplate datetime helpers."""
import datetime as dt

__all__ = ["iso8601_to_datetime"]


def iso8601_to_datetime(strtime):
    """Convert ISO8601 strings to datetime instance."""
    try:
        return dt.datetime.strptime(strtime, "%Y-%m-%dT%H:%M:%S.%fZ")
    except ValueError:
        return dt.datetime.strptime(strtime, "%Y-%m-%dT%H:%M:%SZ")
