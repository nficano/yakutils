"""This module contains logging boilerplate stuff I commonly use."""
import logging.config

BASE_LOGGING_CONFIG = {
    "logging": {
        "version": 1,
        "disable_existing_loggers": True,
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


def setup_logging(self, name: str, cfg=None):
    """Setup application logging.
    
    :param name:
        The name of the logger (typically __name__).
    :param cfg:
        The configuration, defaults to None.
    :return:
        The application logger.
    """
    logging.config.dictConfig(cfg or BASE_LOGGING_CONFIG)
    return logging.getLogger(name)
