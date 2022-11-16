# -*- coding:utf-8 -*-
from pymysql import *


class MyMetaClass(type):
    """元类生成字典"""

    def __new__(cls, class_name, supers_name, attrs):
        create_dict = dict()  # 创建一个新的字典来存放想要的数据
        for key, value in attrs.items():
            if isinstance(value, tuple):
                create_dict[key] = value[0]
        attrs["create_dict"] = create_dict  # 添加新的类属性
        return type.__new__(cls, class_name, supers_name, attrs)


class User(object, metaclass=MyMetaClass):
    uid = ("int unsigned",)
    name = ("varchar(30)",)
    email = ("varchar(30)",)
    password = ("varchar(30)",)

    def create(self):
        # 创建Connection连接
        conn = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
        # 获得Cursor对象
        cs1 = conn.cursor()

        fields = list()

        for key, value in self.create_dict.items():
            fields.append("%s %s" % (key, value))

        # 创建表
        create_sql = """ CREATE TABLE IF NOT EXISTS user(%s);""" % (",".join(fields),)

        print(create_sql)

        cs1.execute(create_sql)

        # 提交
        conn.commit()

        # 关闭
        cs1.close()
        conn.close()

    def insert(self, **kwargs):
        print(kwargs)
        # 创建Connection连接
        conn = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
        # 获得Cursor对象
        cs1 = conn.cursor()

        # 插入数据
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
    user = User()
    user.create()
    user.insert(uid=123, password='pwd', email='test@123.com', name='toby')


if __name__ == '__main__':
    main()
