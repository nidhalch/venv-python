# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup


version = "0.0.1"


with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name="check_redis_sentinel",
    packages=["check_redis_sentinel"],
    entry_points={
        "console_scripts": [
            "check_redis_sentinel = check_redis_sentinel.check_redis_sentinel:main"
        ]
    },
    version=version,
    description=" Check redis sentinel on servers.",
    long_description=long_descr,
    author="DM",
    author_email="nidhal.chabchoubi@dailymotion.com",
    python_requires=">=2.7",
    install_requires="redis>=3.4.1",
)
