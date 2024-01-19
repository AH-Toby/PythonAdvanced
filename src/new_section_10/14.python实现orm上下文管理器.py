#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/15 02:35
# @Author  : toby
# @File    : 14.python实现orm上下文管理器.py
# @Software: PyCharm
# @Desc:
from pymysql import connect, MySQLError


class SqlContext():
    """数据库操作上下文管理器"""

    def __init__(self, host: str, user: str, password: str, port: int = 3306, charset: str = "utf8"):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.charset = charset
        self.conn = None
        self.cursor = None

    def __enter__(self):
        try:
            self.conn = connect(host=self.host, user=self.user, password=self.password, port=self.port,
                                charset=self.charset)
            self.cursor = self.conn.cursor()
            return self.cursor
        except MySQLError as e:
            raise f"数据库连接有问题:{e}"

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if exc_type is None:
                self.conn.commit()  # 提交事务
            else:
                self.conn.rollback()  # 回滚事务

            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()
        except MySQLError as e:
            raise f"数据库关闭有问题:{e}"


def create_table(host: str, user: str, password: str):
    """创建数据库和表"""
    with SqlContext(host, user, password) as cs1:
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


def insert_data(host: str, user: str, password: str, database_name: str):
    """
    插入数据
    """
    with SqlContext(host, user, password) as cs1:
        cs1.execute("CREATE DATABASE IF NOT EXISTS stock_db;")
        cs1.execute(f"USE {database_name};")
        insert_sql = """
        INSERT INTO user (uid,name,email,password) 
        VALUES (456,'test','test@orm.org','pwd');"""
        cs1.execute(insert_sql)


def main():
    host = "192.168.31.111"
    user = "root"
    psw = "mysql"
    database_name = "stock_db"

    # 创建数据表
    create_table(host, user, psw)
    # 向数据表中插入数据
    insert_data(host, user, psw, database_name)


if __name__ == '__main__':
    main()
