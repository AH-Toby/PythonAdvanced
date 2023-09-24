#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/22 14:52
# @Author  : toby
# @File    : 1.编码转换.py
# @Software: PyCharm
# @Desc:

def str_to_bytes(string_content: str) -> bytes:
    return string_content.encode()


def bytes_to_str(byte_content) -> str:
    return byte_content.decode()


if __name__ == '__main__':
    content = "我是字符串"
    bytes_content = str_to_bytes(content)
    print(bytes_content)
    str_content = bytes_to_str(bytes_content)
    print(str_content)
