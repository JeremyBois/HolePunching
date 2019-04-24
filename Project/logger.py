# Project/tools/logger.py


"""
    Some helper function to control logging module interaction without
    knowledge of :class:`logging`.
"""


import logging
from logging.handlers import TimedRotatingFileHandler


__all__ = ['add_file_handler', 'add_file_with_rotation_handler', 'add_stream_handler', 'log_basicConfig']


def add_file_handler(filename: str, level: int=logging.DEBUG, filemode: str='w',
                     parent: str='', fmt: str='', datefmt: str='') -> logging.FileHandler:
    """Add a logger which will write to *filename* events according to
    logging level and *filemode*.

    :param filename: Path of the file used for logging message.
    :param level: Minimal logging level to write to *filename*
                  (default to logging.DEBUG)
    :param filemode: Mode used to control the file
                     (default to 'w')
    :param parent: Select where to attach the new file handler.
                   :data:`None` means to root logger (default).
    :param fmt: Format used for message
                (default to '%(asctime)s %(levelname)-8s: %(name)-35s %(funcName)-25s >> %(message)s')
    :param datefmt: Format used for datetime
                    (default '%Y-%m-%d %H:%M:%S')
    """
    fmt = fmt if fmt else '%(asctime)s %(levelname)-8s: %(name)-35s %(funcName)-25s >> %(message)s'
    datefmt = datefmt if datefmt else '%Y-%m-%d %H:%M:%S'
    file_handler = logging.FileHandler(filename,
                                       filemode, encoding="utf-8")
    file_handler.setLevel(level)
    formatter = logging.Formatter(fmt=fmt,
                                  datefmt=datefmt)
    file_handler.setFormatter(formatter)
    # Add the handler to parent (None return root logger)
    logging.getLogger(parent).addHandler(file_handler)

    return file_handler


def add_file_with_rotation_handler(filename: str, level: int=logging.DEBUG,
                                   when: str='W0', backupCount: int=4, interval: int=1,
                                   parent: str='',
                                   fmt: str='', datefmt: str='') -> TimedRotatingFileHandler:
    """Add a logger which will write to *filename* events according to
    logging level and *filemode*.

    :param filename: Path of the file used for logging message.
    :param level: Minimal logging level to write to *filename*
                  (default to logging.DEBUG)
    :param filemode: Mode used to control the file
                     (default to 'w')
    :param parent: Select where to attach the new file handler.
                   :data:`None` means to root logger (default).
    :param fmt: Format used for message
                (default to '%(asctime)s %(levelname)-8s: %(name)-35s %(funcName)-25s >> %(message)s')
    :param datefmt: Format used for datetime
                    (default '%Y-%m-%d %H:%M:%S')
    """
    fmt = fmt if fmt else '%(asctime)s %(levelname)-8s: %(name)-35s %(funcName)-25s >> %(message)s'
    datefmt = datefmt if datefmt else '%Y-%m-%d %H:%M:%S'
    handler = TimedRotatingFileHandler(filename, when=when, interval=interval,
                                       backupCount=backupCount, encoding="utf-8",
                                       delay=False, utc=False)
    handler.setLevel(level)
    formatter = logging.Formatter(fmt=fmt,
                                  datefmt=datefmt)
    handler.setFormatter(formatter)
    # Add the handler to parent (None return root logger)
    logging.getLogger(parent).addHandler(handler)

    return handler


def add_stream_handler(level=logging.INFO,
                       parent: str='', fmt: str='', datefmt: str='')-> logging.StreamHandler:
    """Add a logger which will write to **stdout** events according to
    logging level.

    :param level: Minimal logging level to write to *filename*
                  (default to logging.DEBUG)
    :param parent: Select where to attach the new file handler.
                   :data:`None` means to root logger (default).
    :param fmt: Format used for message
                (default to '%(levelname)-8s: %(name)-35s %(funcName)-25s >> %(message)s')
    :param datefmt: Format used for datetime
                    (default '%Y-%m-%d %H:%M:%S')
    """
    fmt = fmt if fmt else '%(levelname)-8s: %(name)-35s %(funcName)-25s >> %(message)s'
    datefmt = datefmt if datefmt else '%Y-%m-%d %H:%M:%S'

    cons_handler = logging.StreamHandler()
    cons_handler.setLevel(level)
    formatter = logging.Formatter(fmt=fmt,
                                  datefmt=datefmt)
    cons_handler.setFormatter(formatter)
    logging.getLogger(parent).addHandler(cons_handler)

    return cons_handler


def log_basicConfig(filename: str='log.log', level: int=logging.DEBUG, filemode: str='a',
                    fmt: str='', datefmt: str='') -> None:
    """Configure logging root basic behavior.

    :param filename: Path of the file used for logging message
                     (default to 'log.log')
    :param level: Minimal logging level to write to *filename*
                  (default to logging.DEBUG)
    :param filemode: Mode used to control the file
                     (default to 'a')
    :param fmt: Format used for message
                (default to '%(asctime)s %(levelname)-8s: %(name)-35s %(funcName)-25s >> %(message)s')
    :param datefmt: Format used for datetime
                    (default '%Y-%m-%d %H:%M:%S')

    .. note::
        Default configuration creates a *filename* 'log.log' where main script
        is running. Each new lauch of the script is concatenate to the end of *filename*.
        That is, the log is never removed, new logs are added.

    .. seealso::
        :meth:`logging.basicConfig` and :class:`logging` documentation if
        more control needed over logging initialization.

    """
    fmt = fmt if fmt else '%(asctime)s %(levelname)-8s: %(name)-35s %(funcName)-25s >> %(message)s'
    datefmt = datefmt if datefmt else '%Y-%m-%d %H:%M:%S'
    # Configure root logger with default behavior
    logging.basicConfig(level=level,
                        format=fmt,
                        datefmt=datefmt,
                        filename=filename,
                        filemode=filemode)
