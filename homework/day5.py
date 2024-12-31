# 第一题
def greet(name='xiaoming', greeting='hello'):
    return f'{greeting} {name}'


print(greet())
print(greet('xiaowang'))
print(greet(greeting='hi'))
print(greet(greeting='hey', name='xiaohong'))


# 第二题
def say_hello(*args, **kwargs):
    for arg in args:
        print("hello", arg)

    for k, v in kwargs.items():
        print(f'{k}: {v}')


say_hello("xiaoming", "xiaohong", "xiaowang", name='xiaohei', age=22, city='jinan')


def calculate_total(a, b, c):
    return a + b + c


numbers_tuple = (1, 2, 3)
print(calculate_total(*numbers_tuple))

numbers_dict = {'a': 1, 'b': 2, 'c': 3}
print(calculate_total(**numbers_dict))


# 第三题
class Dog(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self) -> None:
        print(f'{self.name} {self.color}')
    def Bark(self):
        print("wang wang wang")

    def WagTail(self):
        print("摇尾巴")


dahuang = Dog("dahuang", "yellow")
print("%s 是一只%s 的狗狗" % (dahuang.name, dahuang.color))
dahuang.Bark()
dahuang.WagTail()
dahuang
print("%d %d %d %d" % (1, 2, 3, 4))

