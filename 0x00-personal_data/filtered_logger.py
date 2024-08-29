#!/usr/bin/env python3
"""
This module contains a function `filter_datum` that obfuscates specific fields
"""
import logging
from typing import List
from filter_datum import filter_datum


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the formatter with the list of fields to redact.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record and filter sensitive fields.
        """
        return filter_datum(self.fields, self.REDACTION, super().format(record), self.SEPARATOR)
