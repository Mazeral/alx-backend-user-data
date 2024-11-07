#!/usr/bin/env python3
"""Module of filter_datum function
"""

import re


def filter_datum(fields: list, redaction: str,
                 message: str, separator: str) -> str:
    """
    Redacts sensitive fields in a given message.

    This function iterates over a list of fields to be redacted, replaces their
    corresponding values in the message with a provided redaction string, and
    returns the modified message.

    Args:
        fields (list): A list of field names to be redacted
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

    # Initialize an empty string to store the modified message
    new_string = ""

    # Iterate over each field to be redacted
    for field in fields:
        # Use regular expression substitution to replace the field's value
        # with the redaction string
        # The pattern matches the field name followed by any characters
        # except the separator
        new_string = re.sub(f"{field}=[^{re.escape(separator)}]*",
                            f"{field}={redaction}", message)

    # Return the modified message after all fields have been processed
    return new_string
