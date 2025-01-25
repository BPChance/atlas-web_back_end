#!/usr/bin/env python3
""" returns the log message obfuscated """


import re


def filter_datum(fields, redaction, message, separator):
    """ returns the log message obfuscated """
    # pattern for matching fields
    pattern = r"({})=[^{}]+".format("|".join(re.escape(field) for field in fields), re.escape(separator))
    return re.sub(pattern, r"\1={}".format(redaction), message)
