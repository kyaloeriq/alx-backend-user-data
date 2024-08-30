#!/usr/bin/env python3
"""
This module contains a RedactingFormatter class that obfuscates PII data
"""

import re
import logging
from typing import List

# Define the PII_FIELDS constant containing fields considered as PII
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str
        ) -> str:
    """
    Obfuscates specific fields in a log message.
    """
    pattern = '|'.join([
        f'(?<={field}={separator})[^{separator}]+' for field in fields
        ])
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
        # Format the log record using the superclass's format method
        formatted_message = super().format(record) 
        # Apply filtering to the formatted message
        return filter_datum(
            self.fields, self.REDACTION, formatted_message, self.SEPARATOR
        )


def get_logger() -> logging.Logger:
    """
    Creates and configures a logger named 'user_data' that logs up to INFO
    """
    # Create a logger with the name 'user_data'
    logger = logging.getLogger("user_data")
    # Set log level to INFO
    logger.setLevel(logging.INFO)
    # Ensure the logger does not propagate messages to other loggers
    logger.propagate = False
    # Create a StreamHandler and set the RedactingFormatter as the formatter
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    # Add the handler to the logger
    logger.addHandler(stream_handler)
    return logger
