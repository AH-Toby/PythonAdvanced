#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/19 23:01
# @Author  : toby
# @File    : 15.python实现orm动态添加数据.py
# @Software: PyCharm
# @Desc:
from pymysql import connect, MySQLError


# 上下文管理器实现数据库链接和断开
class SQLContext(object):
    def __init__(self, host: str, user: str, psw: str, port: int = 3306, charset: str = 'utf8'):
        self.host = host
        self.user = user
        self.psw = psw
        self.port = port
        self.charset = charset
        self.conn = None
        self.cursor = None

    def __enter__(self):
        try:
            # 链接数据库
            self.conn = connect(host=self.host, user=self.user, password=self.psw, port=self.port, charset=self.charset)
            self.cursor = self.conn.cursor()
            return self.cursor
        except MySQLError as e:
            raise f"数据库链接出错:{e}"

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            # 提交和回滚
            if exc_type is None:
                # 提交
                self.conn.commit()
            else:
                # 回滚
                self.conn.rollback()
            #  关闭链接
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()
        except MySQLError as e:
            raise f"数据库退出出错:{e}"


def create_table(host: str, user: str, password: str, table_name: str, table_attrs: dict):
    """创建数据库和表"""
    with SQLContext(host, user, password) as sql:
        # 选择数据库
        # sql: CREATE DATABASE IF NOT EXISTS stock_db
        sql.execute("CREATE DATABASE IF NOT EXISTS stock_db;")
        sql.execute("USE stock_db;")

        # 整理动态数据
        new_attrs = ",".join([f"{key} {value}" for key, value in table_attrs.items()])
        # 创建数据表
        create_sql = f"""CREATE TABLE IF NOT EXISTS {table_name}({new_attrs});"""
        print(create_sql)
        # 执行语句
        sql.execute(create_sql)


def insert_data(host: str, user: str, password: str, database_name: str, data_attrs: dict):
    """
    插入数据
    """
    with SQLContext(host, user, password) as sql:
        # 选择数据库
        sql.execute("CREATE DATABASE IF NOT EXISTS stock_db;")
        sql.execute(f"USE {database_name};")
        # 数据拼接成标准sql语句
        keys = ",".join([key for key in data_attrs.keys()])
        values = ",".join([f"\"{key}\"" if isinstance(key, str) else str(key) for key in data_attrs.values()])
        print(values)
        # 插入数据
        insert_sql = f"""INSERT INTO info ({keys}) VALUES ({values});"""
        print(insert_sql)
        sql.execute(insert_sql)


def main():
    host = "192.168.31.111"
    user = "root"
    psw = "mysql"
    database_name = "stock_db"

    # 创建数据表
    table_dict = {"uid": "int unsigned", "name": "varchar(30)", "email": "varchar(30)", "password": "varchar(30)"}
    create_table(host, user, psw, "info", table_dict)
    data_dict = {"uid": 123, "name": "test", "email": "test@orm.com", "password": "psw"}
    # 向数据表中插入数据
    insert_data(host, user, psw, database_name, data_dict)


if __name__ == '__main__':
    main()
