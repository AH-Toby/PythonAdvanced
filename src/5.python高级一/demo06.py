class Money(object):
    def __init__(self):
        self.__money = 100

    def getMoney(self):
        return "¥ %d" % self.__money

    def setMoney(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print("error:不是整型数字")


m = Money()
m.setMoney(100)
res = m.getMoney()
print(res)
