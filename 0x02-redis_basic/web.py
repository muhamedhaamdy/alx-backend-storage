#!/usr/bin/env python3
"""Implementing an expiring web cache and tracker"""
from functools import wraps
import redis
import requests
from typing import Callable


client = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """Decorator to count requests"""
    @wraps(method)
    def wrapper(url):
        """ Wrapper for decorator """
        client.incr(f"count:{url}")
        cached_html = client.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')
        html = method(url)
        client.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """Get page"""
    result = requests.get(url)
    return result.text