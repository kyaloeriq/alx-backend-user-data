#!/usr/bin/env python3
"""
This module contains a function `filter_datum` that obfuscates specific fields in a log message.
"""
import re
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
    pattern = r'(?<={0})(.*?)(?={1})'.format(separator, separator)
    return re.sub('|'.join([f'(?<={field}=)[^{separator}]+' for field in fields]), redaction, message)
