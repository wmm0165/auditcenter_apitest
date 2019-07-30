# -*- coding: utf-8 -*-
# @Time : 2019/7/30 14:18
# @Author : wangmengmeng
import time


def wait( func):
    # 可以使函数适配任意多的参数
    def wrapper(*args, **kw):
        time.sleep(5)
        return func(*args, **kw)
    return wrapper


class Test:
    @wait
    def test(self):
        print("被测函数")

    @wait
    def test2(self):
        print("被测函数")


if __name__ == '__main__':
    a = Test()
    a.test()
    a.test2()
