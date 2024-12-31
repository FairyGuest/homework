#  第一题
a = [1, 1, 2, 5, 3, 3, 2]
b = 0
for i in a:
    b = b ^ i
print("出现了一次的数为", b)

#  第二题
for i in range(1,21):
    print(i, end=' ')
print()

#  第三题


def say_hello(count: int):

    """
    此函数用于多次打印“hello”字符，次数取决于参数count
    :param count: int类型，表示打印次数
    :return: None，此函数没有返回值
    """

    print("hello "*count)


say_hello(5)

#  第四题--day3.py
import day_sub

if __name__ == "__main__":
    day_sub.print_hello()
    day_sub.print_line()
    day_sub.print_goodbye()


#  第五题
l1 = [1, 2, 4, 5, 6, 7, 8, 9, 10]
print("初始状态下列表l1为：", l1)
l1.insert(2, 11)  # 在2处插入11
print("此时l1的状态为", l1)
l1.append(11)  # 在最后插入12
print("此时l1的状态为", l1)
l2 = [99, 98, 97]  # 拼接l2
l1.extend(l2)
print("此时l1的状态为", l1)

l1[2] = 3  # 修改索引数据
print("此时l1的状态为", l1)

del l1[-1]  # 删除最后一个数据
print("此时l1的状态为", l1)
l1.remove(99)  # 删除第一个出现的99
print("此时l1的状态为", l1)
print(l1.pop(-2))  # 删除倒数第二个数据，并返回

print(len(l1))  # 列表长度
print(l1.count(1))  # 统计1在列表中出现的次数

l1.sort()  # 升序排序
print("此时l1的状态为", l1)
l1.sort(reverse=True)  # 降序排序
print("此时l1的状态为", l1)
l1.reverse()  # 逆转
print("此时l1的状态为", l1)


#  第六题
m = [1, 1, 2, 2, 3, 3, 4, 5]
n = []
for i in m:
    if i in n:
        n.remove(i)
        continue
    n.append(i)
print("列表中出现次数为1的两个数为：", n)

