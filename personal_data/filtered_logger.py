#!/usr/bin/env python3
""" returns the log message obfuscated """


import re
import logging
import csv
import os
from typing import List
import mysql.connector
from mysql.connector.connection import MySQLConnection


PERSONAL_DATA_DB_USERNAME = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
PERSONAL_DATA_DB_PASSWORD = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
PERSONAL_DATA_DB_HOST = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
PERSONAL_DATA_DB_NAME = os.getenv('PERSONAL_DATA_DB_NAME', 'name')


PII_FIELDS = ("name", "email", "ssn", "phone", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """ format the log record by redacting fields"""
        record.msg = filter_datum(
            self.fields,
            self.REDACTION,
            record.msg,
            self.SEPARATOR
        )
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


def get_logger() -> logging.Logger:
    """ creates and configures a logger for handling sensitive data """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def get_db() -> MySQLConnection:
    """ connect mysql db """
    return mysql.connector.connect(
        user=PERSONAL_DATA_DB_USERNAME,
        password=PERSONAL_DATA_DB_PASSWORD,
        host=PERSONAL_DATA_DB_HOST,
        database=PERSONAL_DATA_DB_NAME
    )
