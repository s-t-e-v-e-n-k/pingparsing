# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

from __future__ import absolute_import, unicode_literals

import logbook
import subprocrunner


LOG_FORMAT_STRING = "[{record.level_name}] {record.channel}: {record.message}"


logger = logbook.Logger("pingparsing lib")
logger.disable()


def set_logger(is_enable):
    if is_enable:
        logger.enable()
    else:
        logger.disable()

    subprocrunner.set_logger(is_enable)

def set_log_level(log_level):
    """
    Set logging level of this module. The module using
    `logbook <http://logbook.readthedocs.io/en/stable/>`__ module for logging.

    :param int log_level:
        One of the log level of the
        `logbook <http://logbook.readthedocs.io/en/stable/api/base.html>`__.
        Disabled logging if the ``log_level`` is ``logbook.NOTSET``.
    :raises LookupError: If ``log_level`` is an invalid value.
    """

    # validate log level
    logbook.get_level_name(log_level)

    if log_level == logbook.NOTSET:
        set_logger(is_enable=False)
    else:
        set_logger(is_enable=True)

    logger.level = log_level
    subprocrunner.set_log_level(log_level)
    