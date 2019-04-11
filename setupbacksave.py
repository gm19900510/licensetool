#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: xingming
# Mail: huoxingming@gmail.com
# Created Time:  2015-12-11 01:25:34 AM
#############################################


from setuptools import setup, find_packages

setup(
    name = "magetool",
    version = "0.0.1",
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