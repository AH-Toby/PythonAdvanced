from collections import Iterable


class MyList(object):
    def __init__(self):
        self.container = []

    def add(self, item):
        self.container.append(item)

    def __iter__(self):
        """拥有这个属性就说明他是一个Iterable"""
        pass


if __name__ == '__main__':
    mylist = MyList()
    print(isinstance(mylist, Iterable))
