#!/usr/bin/env python3
"""
simple helper function to
calculate start and end indexes
"""


def index_range(page: int, page_size: int) -> tuple:
    """ calculate start and end indexes for page and page size """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
