"""This module contains boilerplate datetime helpers."""
import calendar
import datetime as dt

__all__ = [
    "iso8601_to_datetime",
    "date_to_iso8601",
    "datetime_to_iso8601",
    "datetime_to_unixtimestamp",
]


def iso8601_to_datetime(strtime):
    """Convert ISO 8601 strings to datetime instance."""
    try:
        return dt.datetime.strptime(strtime, "%Y-%m-%dT%H:%M:%S.%fZ")
    except ValueError:
        return dt.datetime.strptime(strtime, "%Y-%m-%dT%H:%M:%SZ")


def datetime_to_iso8601(datetime):
    """Convert datetime to ISO 8601 string."""
    if datetime.microsecond > 0:
        return datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    return datetime.strftime("%Y-%m-%dT%H:%M:%SZ")


def date_to_iso8601(date):
    """Convert date to ISO 8601 string."""
    datetime = dt.datetime.combine(date, dt.datetime.min.time())
    if datetime.microsecond > 0:
        return datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    return datetime.strftime("%Y-%m-%dT%H:%M:%SZ")


def datetime_to_unixtimestamp(datetime):
    """Convert datetime to Unix timestamp."""
    return int(calendar.timegm(datetime.timetuple()))
