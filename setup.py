# -*- coding: utf-8 -*-
 
 
"""setup.py: setuptools control."""
 
 
import re
from setuptools import setup
 
 
version = '0.0.1'
 
 
with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")
 
 
setup(
    name = "redis_sentinel_check_oio",
    packages = ["redis_sentinel_check_oio"],
    entry_points = {
        "console_scripts": ['redis_sentinel_check_oio = redis_sentinel_check_oio.check_redis_sentinel_check:main']
        },
    version = version,
    description = " Check redis sentinel on oIo servers.",
    long_description = long_descr,
    author = "DM",
    author_email = "nidhal.chabchoubi@dailymotion.com",
    )
