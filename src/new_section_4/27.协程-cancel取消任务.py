#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/15 15:23
# @Author  : toby
# @File    : 27.协程-cancel取消任务.py
# @Software: PyCharm
# @Desc:

import asyncio


async def cancel_me():
    print('cancel_me(): before sleep')
    try:
        await asyncio.sleep(3600)  # 模拟一个耗时任务
    except asyncio.CancelledError:
        print('cancel_me(): cancel sleep')
        raise
    finally:
        print('cancel_me(): after sleep')


async def main():
    # 通过协程创建一个任务，需要注意的是，在创建任务的时候，就会跳入到异步开始执行
    task = asyncio.create_task(cancel_me())
    # 等待一秒钟
    await asyncio.sleep(1)
    print('main函数休息完了')
    # 发出取消任务的请求
    task.cancel()
    try:
        await task  # 因为任务被取消，触发了异常
    except asyncio.CancelledError:
        print("main(): cancel_me is cancelled now")


asyncio.run(main())

'''运行结果为：
cancel_me(): before sleep
main函数休息完了
cancel_me(): cancel sleep
cancel_me(): after sleep
main(): cancel_me is cancelled now
'''
