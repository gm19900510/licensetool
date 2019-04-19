#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: gm
# Mail: 1025304567@qq.com
# Created Time: 2019-04-11 15:37:04
#############################################


from setuptools import setup, find_packages

setup(
    name = "licensetool",
    version = "0.0.7",
    keywords = ("pip", "license","licensetool", "tool", "gm"),
    description = "设备指纹获取、license生成、指纹与有效期验证工具",
    long_description = "设备指纹获取、license生成、指纹与有效期验证工具",
    license = "MIT Licence",

    url = "https://github.com/gm19900510/licensetool",
    author = "gm",
    author_email = "1025304567@qq.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ['chardet']
)