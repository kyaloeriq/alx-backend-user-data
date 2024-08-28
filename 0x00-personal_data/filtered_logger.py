#!/usr/bin/env python3
"""
This module contains a function `filter_datum` that obfuscates specific fields
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                    separator: str) -> str:
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
    pattern = '|'.join([
        f'(?<={field}=)[^{separator}]+' for field in fields
    ])
    return re.sub(pattern, redaction, message)
