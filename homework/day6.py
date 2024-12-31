# 1、练习封装案例（和上课保持一致即可）
# 2、练习私有属性和私有方法（和上课保持一致即可）
# 3、练习单继承，多重继承案例（和上课保持一致即可）
# 4、实现单例模式（和上课保持一致即可）
# 5、通过try进行异常捕捉，确保输入的内容一定是一个整型数，然后判断该整型数是否是对称数，12321就是对称数，123321也是对称数，否则就打印不是，非整型抛异常，不是对称数抛异常
# 第一题
class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count <= 0:
            print("子弹为0")

            return
        self.bullet_count -= 1
        print("%s 发射子弹[%d]" % (self.model, self.bullet_count))


class Soldier:
    def __init__(self, name, gun: Gun = None):
        self.name = name
        self.gun = gun

    def fire(self):
        if self.gun is None:
            print("%s 还没有枪" % (self.name))

            return

        print("gogogo! %s" % (self.name))

        self.gun.add_bullet(50)

        self.gun.shoot()


ak47 = Gun('ak47')
xusanduo = Soldier('xusanduo')
xusanduo.fire()
xusanduo.gun = ak47
xusanduo.fire()


# 第二题
class Women:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def __secret(self):
        print(f'{self.name} 年龄{self.__age}')

    def boy_friend(self):
        self.__secret()


xiaohong = Women('xiaohong', 20)
xiaohong.boy_friend()


# 第三题——单继承
class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def sleep(self):
        print("睡")

    def run(self):
        print('跑')


class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def bark(self):
        print("汪汪叫")

    def run(self):
        super().run()
        print("%s跑得快" % self.name)


class XiaoTainQuan(Dog):
    def __init__(self, name, color, age):
        super().__init__(name, color)
        self.age = age

    def fly(self):
        print("%s 飞天" % self.name)


xiaotian = XiaoTainQuan('哮天', '黑色', 2000000)
xiaotian.fly()


# 第三题——多继承
class A:
    def test(self):
        print('A test')

    def demo(self):
        print('A demo')


class B:
    def test(self):
        print('B test')

    def demo(self):
        print('B demo')


class C(A, B):
    def test(self):
        print('C test')


c = C()
c.test()
print(C.__mro__)


# 第四题
class MusicPlayer(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)  # 类似于malloc

        return cls.instance

    def __init__(self, name):
        self.name = name


player1 = MusicPlayer('Never gonna give you up')
player2 = MusicPlayer('皮囊')
print(id(player1))
print(id(player2))
if id(player1) == id(player2):
    print("单例模式已实现")

# 第五题
try:
    number = int(input("请输入一个整数"))
    number_str = str(number)
    str_1 = number_str[0:len(number_str) // 2]
    if len(number_str) % 2 == 0:
        str_2 = number_str[len(number_str) // 2:]
    else:
        str_2 = number_str[len(number_str) // 2 + 1:]
    str_2 = str_2[::-1]
    if str_1 == str_2:
        print('对称数')
    else:
        print("非对称数")
except ValueError:
    print("类型错误，请输入整数")

    
