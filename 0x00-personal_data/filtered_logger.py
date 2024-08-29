#!/usr/bin/env python3
"""
This module contains a RedactingFormatter class that obfuscates specific fields in log messages.
"""

import re
import logging
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscates specific fields in a log message.

    Args:
        fields (List[str]): Fields to obfuscate.
        redaction (str): String to replace the field values with.
        message (str): The log message.
        separator (str): Separator character used in the log message.

    Returns:
        str: The obfuscated log message.
    """
    pattern = '|'.join([f'(?<={field}={separator})[^{separator}]+' for field in fields])
    return re.sub(pattern, redaction, message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the formatter with the list of fields to redact.
        """
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record and filter sensitive fields.
        """
        return filter_datum(self.fields, self.REDACTION, super().format(record), self.SEPARATOR)
