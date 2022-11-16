# -*- coding:utf-8 -*-
from pymysql import *


def create():
    create_dict = {"uid": "int unsigned", "name": "varchar(30)", "email": "varchar(30)", "password": "varchar(30)"}

    # 创建Connection连接
    conn = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
    # 获得Cursor对象
    cs1 = conn.cursor()

    fields = list()

    for key, value in create_dict.items():
        fields.append("%s %s" % (key, value))

    # 创建表
    # create_sql = """ CREATE TABLE IF NOT EXISTS user(uid int unsigned,name varchar(30),email varchar(30),password varchar(30));"""
    create_sql = """ CREATE TABLE IF NOT EXISTS user(%s);""" % (",".join(fields),)

    print(create_sql)

    cs1.execute(create_sql)

    # 提交
    conn.commit()

    # 关闭
    cs1.close()
    conn.close()


def insert(**kwargs):
    print(kwargs)
    # 创建Connection连接
    conn = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
    # 获得Cursor对象
    cs1 = conn.cursor()

    # 插入数据
    # insert_sql = """ insert into user (uid,name,email,password) values (123,'oldyang','test@orm.org','pwd');"""
    keys = list()
    values = list()

    for key, value in kwargs.items():
        keys.append(key)
        # 如果是Int转成字符串
        if isinstance(value, int):
            # 说明 int
            values.append(str(value))
        else:
            values.append(""" "%s" """ % value)

    insert_sql = """ insert into user (%s) values (%s);""" % (",".join(keys), ",".join(values))

    print(insert_sql)

    cs1.execute(insert_sql)

    # 提交
    conn.commit()

    # 关闭a
    cs1.close()
    conn.close()


def main():
    create()

    insert(uid=123, password='pwd', email='test@123.com', name='toby')


if __name__ == '__main__':
    main()
