#!/usr/bin/env python3
""" module to enhance paginated dataset"""


from typing import List
import math


class Server:
    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ get a paginated dataset and pagination info """
        data = self.get_page(page, page_size)

        items = len(self.dataset())
        total_pages = math.ceil(items / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
