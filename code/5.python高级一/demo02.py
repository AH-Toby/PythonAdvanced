class Person(object):
    def __init__(self, name, age, taste):
        self.name = name
        self._age = age
        self.__taste = taste

    def showperson(self):
        print(self.name)
        print(self._age)
        print(self.__taste)

    def dowork(self):
        self._work()
        self.__away()

    def _work(self):
        print('my _work')

    def __away(self):
        print('my __away')


p = Person(name="lisi", age=18, taste="哈哈")
print(p.name)
print(p._age)
# 下面的方法不能访问
# print(p.__taste)
# 按照下面的方法可以访问
print(p._Person__taste)
