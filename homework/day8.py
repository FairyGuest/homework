# 1、完成二叉树的建树，前序，中序，后序，层序遍历
# 2、完成sorted的练习
#
# 难度作业：
# 3、完成快速排序，堆排序
import random
import time
from operator import itemgetter, attrgetter


# 第一题
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None
        self.help_list = []

    def build_tree(self, node: Node):  # 建树
        if self.root is None:
            self.root = node
            self.help_list.append(node)
        else:
            self.help_list.append(node)
            if self.help_list[0].left is None:
                self.help_list[0].left = node
            else:
                self.help_list[0].right = node
                self.help_list.pop(0)

    def pre_order(self, current_node: Node):
        if current_node is None:
            return
        print(current_node.value, end=' ')
        self.pre_order(current_node.left)
        self.pre_order(current_node.right)

    def in_order(self, current_node: Node):
        if current_node is None:
            return
        self.in_order(current_node.left)
        print(current_node.value, end=' ')
        self.in_order(current_node.right)

    def post_order(self, current_node: Node):
        if current_node is None:
            return
        self.post_order(current_node.left)
        self.post_order(current_node.right)
        print(current_node.value, end=' ')

    def level_order(self):
        help_list = []
        if self.root is None:
            return
        help_list.append(self.root)
        while len(help_list):
            print(help_list[0].value, end=' ')
            if help_list[0].left:
                help_list.append(help_list[0].left)
            if help_list[0].right:
                help_list.append(help_list[0].right)
            help_list.pop(0)


node_list = [Node(x) for x in range(10)]
tree = Tree()
for node in node_list:
    tree.build_tree(node)

print('前序遍历为：')
tree.pre_order(tree.root)
print()

print('中序遍历为：')
tree.in_order(tree.root)
print()

print('后续遍历为：')
tree.post_order(tree.root)
print()

print('层序遍历为：')
tree.level_order()
print()
# 第二题
list_1 = [random.randint(1, 100) for _ in range(10)]
list_2 = sorted(list_1)
print(list_1)
print(list_2)

str_1 = 'Hello World! Baba Lala Baba'
str_list = str_1.split(' ')
str_list.sort(key=str.lower)
print(str_list)

student_tuples = [
    ('jane', 'B', 12),
    ('john', 'A', 15),
    ('dave', 'B', 10),
]

print(sorted(student_tuples, key=lambda tup: tup[1]))  # 以成绩为基准
print(sorted(student_tuples, key=lambda tup: tup[2]))  # 以年龄为基准
print(sorted(student_tuples, key=lambda tup: (tup[1], tup[2])))  # 先以成绩，后以年龄为基准


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        """
        相对于__str__来说，更方便，可以返回非字符串类型
        :return: tuple
        """
        return repr((self.name, self.grade, self.age))


student_list = [
    Student('jane', 'A', 12),
    Student('john', 'B', 15),
    Student('dave', 'B', 10),
]

print(sorted(student_list, key=lambda student: student.name))  # 按照名字排序
print(sorted(student_list, key=lambda student: student.grade))  # 按照成绩排序
print(sorted(student_list, key=lambda student: student.age))  # 按照年龄排序
print(sorted(student_list, key=lambda student: (student.grade, student.age)))  # 先按照成绩，再按照年龄排序

print(sorted(student_tuples, key=itemgetter(0)))
print(sorted(student_list, key=attrgetter('grade', 'age')))

dict_1 = {'Li': ['M', 7],
          'Zhang': ['E', 2],
          'Wang': ['P', 3],
          'Du': ['C', 2],
          'Ma': ['C', 9],
          'Zhe': ['H', 7]}
print(sorted(dict_1.items(), key=lambda x: x[1][1]))


# 第三题
class Sort:
    def __init__(self, n):
        """
        n是排序的数量
        :param n:
        """
        self.len = n
        self.arr = [random.randint(1, 99) for _ in range(n)]

    def partition(self, l, r):
        arr = self.arr
        k = l
        i = l
        random_pos = random.randint(l, r)  # 随机选取一个位置的值进行分治
        arr[random_pos], arr[r] = arr[r], arr[random_pos]
        for i in range(l, r):
            if arr[i] < arr[r]:
                arr[i], arr[k] = arr[k], arr[i]
                k += 1
        arr[k], arr[r] = arr[r], arr[k]
        return k

    def quick_sort(self, l, r):
        if l < r:
            pivot = self.partition(l, r)
            self.quick_sort(l, pivot - 1)
            self.quick_sort(pivot + 1, r)

    def adjust_max_heap(self, pos, arr_len):
        """
        把子树调整成大根堆
        :param pos: 被调整的元素位置
        :param arr_len: 当时列表长度
        :return:
        """
        arr = self.arr
        parent = pos  # 从pos开始子树
        child = 2 * parent + 1  # parent的左子节点
        while child < arr_len:  # 左孩子小于列表长度
            if child + 1 < arr_len and arr[child] < arr[child + 1]:  # 判断右孩子存在和左孩子小于右孩子
                child += 1  # 右孩子和parent换
            if arr[child] > arr[parent]:  # 如果孩子大于父亲，则交换且父变子，子变孙
                arr[child], arr[parent] = arr[parent], arr[child]
                parent = child
                child = 2 * parent + 1  # 更新孩子pos
            else:
                break

    def adjust_min_heap(self, pos, arr_len):
        """
        把子树调整成小根堆
        :param pos: 被调整的元素位置
        :param arr_len: 当时列表长度
        :return:
        """
        arr = self.arr
        parent = pos
        child = 2 * parent + 1
        while child < arr_len:
            if child + 1 < arr_len and arr[child] > arr[child + 1]:  # 如果左孩子大于右孩子
                child += 1
            if arr[child] < arr[parent]:  # 如果孩子小于父亲，则调整
                arr[child], arr[parent] = arr[parent], arr[child]
                parent = child
                child = 2 * parent + 1
            else:
                break

    def heap_sort_max(self):
        for parent in range(self.len // 2 - 1, -1, -1):  # 先对初始状态下进行一次调整
            self.adjust_max_heap(parent, self.len)
        arr = self.arr
        arr[0], arr[-1] = arr[-1], arr[0]  # 交换头与尾，并让堆排序长度减一
        for arr_len in range(self.len - 1, 1, -1):
            self.adjust_max_heap(0, arr_len)
            arr[0], arr[arr_len - 1] = arr[arr_len - 1], arr[0]

    def heap_sort_min(self):
        for parent in range(self.len // 2 - 1, -1, -1):
            self.adjust_min_heap(parent, self.len)
        arr = self.arr
        arr[0], arr[-1] = arr[-1], arr[0]
        for arr_len in range(self.len - 1, 1, -1):
            self.adjust_min_heap(0, arr_len)
            arr[0], arr[arr_len - 1] = arr[arr_len - 1], arr[0]

    def test_time_test(self, sort_func, *args, **kwargs):
        """
        回调函数
        :param sort_func: 排序所用的函数
        :param args: 排序所用函数的参数
        :param kwargs: 排序所用函数的参数--以字典形式
        :return:
        """
        start_time = time.time()
        sort_func(*args, **kwargs)
        end_time = time.time()
        print(f'{sort_func}耗时{end_time - start_time}')


count = 10000
my_sort = Sort(count)
print('原始数据：',my_sort.arr)
my_sort.quick_sort(0, 10 - 1)
print('快排后：', my_sort.arr)
my_sort.heap_sort_max()
print('大根堆：', my_sort.arr)
my_sort.heap_sort_min()
print('小根堆', my_sort.arr)
my_sort.test_time_test(my_sort.heap_sort_max)
my_sort.test_time_test(my_sort.quick_sort, 0, count - 1)
