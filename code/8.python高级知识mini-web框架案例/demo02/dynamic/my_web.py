# -*- coding:utf-8 -*-
import re
from pymysql import *
from urllib.parse import unquote  # 地址栏上的信息进行解码

address_params = dict()  # 路由表


def route(url):
    def set_func(func):
        def call_func(*args, **kwargs):
            return func(*args, **kwargs)

        address_params[url] = func
        return call_func

    return set_func


@route(r'/index.html')
def index(match):
    """返回index.py需要的页面内容"""
    with open(r"./templates/index.html") as f:
        content = f.read()

    row_str = """
    <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>
                <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="%s">
            </td>
            </tr>
        """

    # 1.创建connection连接
    conn = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
    # 2.获得Cursor对象
    cs1 = conn.cursor()
    # 3.执行sql
    cs1.execute("select * from info;")

    # 拿到数据
    tables_str = cs1.fetchall()

    # 关闭
    cs1.close()
    conn.close()

    # 拼接数据
    data_from_mysql = ""

    for temp in tables_str:
        data_from_mysql += row_str % (temp[0], temp[1], temp[2], temp[3], temp[4], temp[5], temp[6], temp[7], temp[1])

    content = re.sub(r"\{%content%\}", data_from_mysql, content)
    return content


@route('/center.html')
def center(match):
    """返回center.py需要的页面内容"""
    with open(r"./templates/center.html") as f:
        content = f.read()

    row_str = """
    <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>
                <a type="button" class="btn btn-default btn-xs" href="/update/%s.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
            </td>
            <td>
                <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="%s">
            </td>
        </tr>
    """

    # 1.创建connection连接
    conn = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
    # 2.获得Cursor对象
    cs1 = conn.cursor()
    # 3.执行sql
    cs1.execute(
        "select i.code,i.short,i.chg,i.turnover,i.price,i.highs,f.note_info from info as i , focus as f where i.id = f.info_id;")

    # 拿到数据
    tables_str = cs1.fetchall()

    # 关闭
    cs1.close()
    conn.close()

    # 拼接数据
    data_from_mysql = ""

    for temp in tables_str:
        data_from_mysql += row_str % (temp[0], temp[1], temp[2], temp[3], temp[4], temp[5], temp[6], temp[0], temp[0])

    content = re.sub(r"\{%content%\}", data_from_mysql, content)
    return content


@route(r'/add/(\d+).html')
def add_method(match):
    code = match.group(1)

    insert_sql = """insert into focus (info_id) select id from info where  code = %s;"""
    search_sql = """select * from focus where info_id in(select id from info where code = %s);"""

    # 1. 连接 数据
    # 2. 查询数据是否存在,如果不存在,那么插入,如果存在,那么提示用户已经插入
    # 3. 关闭
    # 创建Connection连接
    conn = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
    # 获得Cursor对象
    cs1 = conn.cursor()

    cs1.execute(search_sql, (code,))

    if cs1.fetchone():
        # 说明有数据
        # 返回数据已存在
        cs1.close()
        conn.close()

        return "数据已存在"
    else:
        # 没有数据
        # 插入数据
        cs1.execute(insert_sql, (code,))
        # 提交
        conn.commit()
        cs1.close()
        conn.close()
        return "添加成功"


@route(r'/del/(\d+).html')
def del_method(match):
    code = match.group(1)
    # 创建Connection连接
    conn = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
    # 获得Cursor对象
    cs1 = conn.cursor()
    del_sql = """ delete from focus where info_id in(select id from info where code=%s);"""

    cs1.execute(del_sql, (code,))
    conn.commit()

    cs1.close()
    conn.close()
    return "删除成功"


@route(r'/update/(\d+).html')
def update_method(match):
    code = match.group(1)

    with open("./templates/update.html") as f:
        content = f.read()

    # 替换{%code%}
    content = re.sub(r'\{%code%\}', code, content)

    # 从数据库找到备注信息,进行替换
    # { % note_info %}
    note_sql = """ select note_info from focus where info_id in(select id from info where code = %s);"""

    # 1 .连接 数据 库
    # 2 . 执行我们sql
    # 3. 关闭
    # 创建Connection连接
    conn = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
    # 获得Cursor对象
    cs1 = conn.cursor()
    cs1.execute(note_sql, (code,))

    # 拿到信息
    row_note = cs1.fetchone()
    # 关闭
    cs1.close()
    conn.close()

    # 替换我们的数据
    content = re.sub(r'\{%note_info%\}', row_note[0], content)

    return content


@route(r"/update/(\d+)/(.*).html")
def update_data_method(match):
    code = match.group(1)
    content = unquote(match.group(2))

    note_sql = """update focus set note_info = %s where info_id in (select id from info where code = %s);"""

    # 直接 更新
    # 创建Connection连接
    conn = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
    # 获得Cursor对象
    cs1 = conn.cursor()
    cs1.execute(note_sql, (content, code))
    conn.commit()
    # 关闭
    cs1.close()
    conn.close()

    return "更新完成"


def application(environ, start_response):
    """
    :param environ: http给我们的mini框架传数据
    :param start_response: 这个给http传数据
    :return:
    """

    start_response('200 ok', [('Content-Type', 'text/html')])
    # 这里更具不同的地址（url）地址去进行相应的处理
    url = environ['file_name']
    print("获得的url地址是：%s" % url)

    try:
        for url_match, method in address_params.items():
            match = re.match(url_match, url)
            if match:
                return method(match)
        else:
            return 'page not find'
    except Exception as e:
        return "%s" % e
