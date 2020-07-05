class Person(object):
    def foo(self):
        """
        实例方法
        :return:
        """
        print(id(self))  # 用来查看对象的id

    @staticmethod
    def static_foo():
        """
        静态方法
        :return:
        """
        print("in static")

    @classmethod
    def class_foo(cls):
        """
        类方法
        :return:
        """
        print("in class")


p1 = Person()
p2 = Person()
p1.foo()
p2.foo()

p1.static_foo()
p1.class_foo()

# 运行顺序 实例->类对象->类对象方法
# 可以使用__class__来调用类对象方法
p1.__class__.class_foo()
