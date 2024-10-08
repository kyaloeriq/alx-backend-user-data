#!/usr/bin/env python3
"""
This module contains:
- RedactingFormatter class to obfuscate PII data in log messages.
- get_db function to securely connect to a MySQL database.
- main function to retrieve and display user data from the database.
"""

import os
import re
import logging
import mysql.connector
from typing import List
from mysql.connector import connection

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
    Creates and configures a logger named 'user_data' that logs up to INFO.
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


def get_db() -> connection.MySQLConnection:
    """
    Returns a connector to the database using credentials
    """
    # Retrieve database credentials from environment variables
    username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    database = os.getenv('PERSONAL_DATA_DB_NAME')

    # Connect to the database using the retrieved credentials
    connection = mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=database
    )

    return connection


def main() -> None:
    """
    Retrieves all rows in the users table and displays each row
    """
    # Obtain the logger
    logger = get_logger()

    # Get the database connection
    db = get_db()

    try:
        # Perform database operations
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users;")
        rows = cursor.fetchall()

        for row in rows:
            # Construct a formatted log message for each row
            message = (
                f"name={row[0]}; email={row[1]}; phone={row[2]}; "
                f"ssn={row[3]}; password={row[4]}; "
                f"ip={row[5]}; last_login={row[6]}; "
                f"user_agent={row[7]};"
            )
            # Log the message (with PII fields redacted)
            logger.info(message)

    finally:
        cursor.close()
        db.close()


if __name__ == "__main__":
    main()
