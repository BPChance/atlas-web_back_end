#!/usr/bin/env python3
""" returns the log message obfuscated """


import re
import logging
from typing import List


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """ format the log record by redacting fields"""
        record.msg = filter_datum(self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super().format(record)

def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str
) -> str:
    """ returns the log message obfuscated """
    # pattern for matching fields
    pattern = r"({})=[^{}]+".format(
        "|".join(re.escape(field) for field in fields),
        re.escape(separator)
    )
    return re.sub(pattern, r"\1={}".format(redaction), message)
