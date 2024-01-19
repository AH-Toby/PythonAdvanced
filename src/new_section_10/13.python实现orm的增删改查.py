#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/12 00:28
# @Author  : toby
# @File    : 13.python实现orm的增删改查.py
# @Software: PyCharm
# @Desc: Python实现基本sql
from pymysql import *


def create_table(host: str, user: str, password: str, database_name: str, port: int = 3306, charset: str = "utf8"):
    """创建数据库和表"""
    # 创建数据库连接
    conn = connect(host=host, port=port, user=user, password=password, charset=charset)

    # 获取Cursor对象
    cs1 = conn.cursor()

    # 选择数据库
    # sql: CREATE DATABASE IF NOT EXISTS stock_db
    cs1.execute("CREATE DATABASE IF NOT EXISTS stock_db;")
    cs1.execute("USE stock_db;")

    # 创建数据表
    create_sql = """
    CREATE TABLE IF NOT EXISTS user(
        uid int unsigned,
        name varchar(30),
        email varchar(30),
        password varchar(30)
        );"""
    cs1.execute(create_sql)

    # 提交sql
    conn.commit()

    # 关闭数据库连接
    cs1.close()
    conn.close()


def insert_data(host: str, user: str, password: str, database_name: str, port: int = 3306, charset: str = "utf8"):
    """
    插入数据
    """
    # 1.创建数据库连接获取数据库对象
    conn = connect(host=host, port=port, user=user, password=password, charset=charset, database=database_name)

    # 2.获取数据库操作对象
    cs1 = conn.cursor()

    # 3.执行插入数据sql
    insert_sql = """
    INSERT INTO user (uid,name,email,password) 
    VALUES (123,'test','test@orm.org','pwd');"""
    cs1.execute(insert_sql)

    # 4.提交执行语句xs
    conn.commit()

    # 5.关闭数据库连接
    cs1.close()
    conn.close()


def main():
    host = "192.168.31.111"
    user = "root"
    psw = "mysql"
    database_name = "stock_db"

    # 创建数据表
    create_table(host, user, psw, database_name)
    # 向数据表中插入数据
    insert_data(host, user, psw, database_name)


if __name__ == '__main__':
    main()
