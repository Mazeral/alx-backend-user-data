#!/usr/bin/env python3
"""
Module containing the filter_datum function and RedactingFormatter class.

This module provides functionality to redact sensitive information in log
messages using a custom logging formatter.
"""

import re
import logging
from typing import List


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class to redact sensitive fields in log messages.

    This class formats log messages by replacing the values of sensitive fields
    with a redaction string before outputting the log message.

    Attributes:
        fields (List[str]): A list of field names to be redacted in the log
            messages.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initializes the RedactingFormatter with a list of fields to redact.

        Args:
            fields (List[str]): The list of field names to be redacted in log
            messages.
        """
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """
        Formats a log record, redacting sensitive fields before logging.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The formatted log message with sensitive fields redacted.
        """
        # Redact sensitive information in the log message
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.msg, self.SEPARATOR)
        return super().format(record)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Redacts sensitive fields in a given message.

    This function iterates over a list of fields to be redacted, replaces their
    corresponding values in the message with a provided redaction string, and
    returns the modified message.

    Args:
        fields (List[str]): A list of field names to be redacted
        (e.g., 'name', 'email').

        redaction (str): The string to replace the sensitive field values with.
        message (str): The input message containing field-value pairs
        (e.g., 'name=bob;email=bob@dylan.com;...').

        separator (str): The character separating field-value pairs in the
        message (e.g., ';').

    Returns:
        str: The modified message with sensitive fields redacted.

    Example:
        fields = ['password', 'date_of_birth']
        redaction = 'xxx'
        message = 'name=bob;email=bob@dylan.com;password=mypassword;
        date_of_birth=1990-01-01;'
        separator = ';'
        print(filter_datum(fields, redaction, message, separator))
        # Output: 'name=bob;email=bob@dylan.com;password=xxx;
        date_of_birth=xxx;'
    """
    # Redact the sensitive fields in the message
    for field in fields:
        message = re.sub(f"{field}=[^{re.escape(separator)}]*",
                         f"{field}={redaction}", message)
    return message


def get_logger() -> logging.Logger:
    """
    Creates and configures a logger named 'user_data' for logging user data.

    This function sets up a logger with the following characteristics:
        - Named 'user_data'.
        - Log level is set to INFO.
        - It does not propagate messages to other loggers.
        - Uses a stream handler to log messages to the console.
        - Applies a custom RedactingFormatter to redact sensitive fields.

    Returns:
        logging.Logger: A configured logger instance with redaction enabled.
    """

    # Creating a logger named "user_data"
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)

    # Ensures that the logger doesn't propagate messages to other loggers
    logger.propagate = False

    # RedactingFormatter with PII_FIELDS
    formatter = RedactingFormatter(fields=PII_FIELDS)

    # Creating a stream handler to log to the console and attaching
    # the formatter
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    # Attaching the handler to the logger
    logger.addHandler(stream_handler)

    return logger
