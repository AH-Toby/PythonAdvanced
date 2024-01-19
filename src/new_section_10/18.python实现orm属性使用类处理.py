#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/20 01:12
# @Author  : toby
# @File    : 18.python实现orm属性使用类处理.py
# @Software: PyCharm
# @Desc:
from pymysql import connect, MySQLError


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


class Field(object):
    def __init__(self, data):
        self.data = data


class MyMateClass(type):
    def __new__(cls, class_name, class_bases, class_dict):
        # 直接生成sql语句
        new_attrs = ",".join([f"{key} {value.data}" for key, value in class_dict.items() if isinstance(value, Field)])
        class_dict["create_sql"] = new_attrs
        class_dict["table_name"] = class_name.lower()  # 添加表名
        return super().__new__(cls, class_name, class_bases, class_dict)


# 基类
class TableBase(object, metaclass=MyMateClass):
    def create_table(self, host: str, user: str, password: str):
        """创建数据库和表"""
        with SQLContext(host, user, password) as sql:
            # 选择数据库
            # sql: CREATE DATABASE IF NOT EXISTS stock_db
            sql.execute("CREATE DATABASE IF NOT EXISTS stock_db;")
            sql.execute("USE stock_db;")
            # 创建数据表
            create_sql = f"""CREATE TABLE IF NOT EXISTS {self.table_name}({self.create_sql});"""
            print(create_sql)
            # 执行语句
            sql.execute(create_sql)

    def insert_data(self, host: str, user: str, password: str, database_name: str, data_attrs: dict):
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
            # 插入数据
            insert_sql = f"""INSERT INTO {self.table_name} ({keys}) VALUES ({values});"""
            print(insert_sql)
            sql.execute(insert_sql)


class Usr(TableBase):
    # 将创建表的功能交给元类处理
    # 属性用类来处理可以更好区分
    uid = Field("int unsigned", )
    name = Field("varchar(30)", )
    email = Field("varchar(30)", )
    password = Field("varchar(30)", )


def main():
    host = "192.168.31.111"
    user = "root"
    psw = "mysql"
    database_name = "stock_db"

    # 创建数据表
    user_obj = Usr()
    user_obj.create_table(host, user, psw)
    data_dict = {"uid": 123, "name": "test", "email": "test@orm.com", "password": "psw"}
    # 向数据表中插入数据
    user_obj.insert_data(host, user, psw, database_name, data_dict)


if __name__ == '__main__':
    main()
