"""This module contains boilerplate logging helpers."""
import logging.config

SANE_BASE_LOGGING_CONFIG = {
    "logging": {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "simple": {"format": "%(asctime)s: %(message)s"},
            "verbose": {
                "format": "%(asctime)s [%(levelname)s] %(module)s %(message)s"
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "simple",
                "stream": "ext://sys.stdout",
            }
        },
        "root": {"level": "DEBUG", "handlers": ["console"]},
    }
}


def setup_logging(self, name="root", cfg=None):
    """Create a logger.

    :param name:
        The name of the logger, defaults to 'root'.
    :param cfg:
        The configuration ``dict``, defaults to ``SANE_BASE_LOGGING_CONFIG``.
    :return:
        A logger with the specified name.
    """
    logging.config.dictConfig(cfg or SANE_BASE_LOGGING_CONFIG)
    return logging.getLogger(name)
