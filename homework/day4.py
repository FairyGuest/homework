# 第一题
# 元组
tuple1 = ("liu", 1, 2, "liu")
for i in tuple1:
    print(i)
print(tuple1.index("liu"))
print(tuple1.count("liu"))
print(len(tuple1))

tuple2 = ("xiaoming", 22, 1.83)
print("%s 年龄是%d 身高是%.2f m" % tuple2)
info_tuple2 = "%s 年龄是%d 身高是%.2f m" % tuple2
print(info_tuple2)
print(f'使用f{info_tuple2}')

# 字典
xiaowang_dict = {"name": "xiaowang", "age": 22}
print(id(xiaowang_dict))
print(xiaowang_dict["name"])
xiaowang_dict["gender"] = "male"
print(xiaowang_dict)
xiaowang_dict["age"] = 23
print(xiaowang_dict)
del xiaowang_dict["gender"]
print(xiaowang_dict)
print(len(xiaowang_dict))
temp_dict = {"height": 1.83, "age": 80}
xiaowang_dict.update(temp_dict)
print(xiaowang_dict)
xiaowang_dict.clear()
print(xiaowang_dict)
print(id(xiaowang_dict))

xiaoming_dict = {"name": "xiaoming", "qq": "12345678", "phone": "13599228"}
for k in xiaowang_dict:
    print(k, xiaowang_dict[k])
for k, v in xiaowang_dict.items():
    print(f'键{k},值{v}')
for k in xiaoming_dict.keys():
    print(k)
for v in xiaowang_dict.values():
    print(v)

card_list = [
        {"name": "zhangsan",
         "qq": "12345",
         "phone": "110"},
        {"name": "lisi",
         "qq": "54321",
         "phone": "10086"}
    ]
for card in card_list:
    print(card)

k, v, w = (1, 2, 3)
print(k, v, w)

# 字符串
s1 = "string*"
print(s1.isalnum())
s2 = "12345"
print(s2.isdecimal())

s3 = 'abc abc 哈哈哈'
print(s3.split())
s4 = 'abc,abc,hhh'
print(s4.split(','))
s5 = 'abc\nabc\nhhh'
print(s5.splitlines())
s6 = 'abc\rabc\rhhh'
print(s6.splitlines(True))
str_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(','.join(str_list))

number_str = '0123456789'
print(number_str[2:6])
print(number_str[2:])
print(number_str[:2])
print(number_str[:])
print(number_str[::2])
print(number_str[1::2])
print(number_str[-1])
print(number_str[2:-1])
print(number_str[-2:])
print(number_str[::-1])

hello_str = "hello hello world"
print(len(hello_str))
print(hello_str.count("llo"))
print(hello_str.find("abc"))
print(hello_str.index("llo"))
# 集合
set1 = set()
print(type(set1))
set2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)
x = fruits.copy()
print(id(x))
print(id(fruits))
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)
x.difference_update(y)
print(x)
fruits.discard("banana")
print(fruits)
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
result = x.intersection(y, z)
print(result)
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
z = x.symmetric_difference(y)
print(z)
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
z = x.union(y)
print(z)
print('apple' in z)
print(x - y)
print(x | y)
print(x & y)
print(x ^ y)

# 第二题
list_2_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_2_2 = [1, 5, 6, 7, 8, 9, 10, 11, 12]

print(list(set(list_2_1) & set(list_2_2)))

# 第三题
a = [1, 8, 4, 7, 4, 4, 4, 4, 6, 4, 10]
a.sort()
print(a[len(a)//2])

# 第四题
# 相同点：均是可迭代的容器，且支持索引访问和嵌套;均支持推导式
# 不同点：列表与字典可变，元组不可变;列表与元组允许重复元素，字典的键唯一;内置方法不同。

# 第五题
tuple_5 = (1, 2, 3)
set_5 = {4, 5, 6}
list_5 = list(tuple_5)+list(set_5)
print(list_5)

# 第六题
list_6 = [1, 2, 3, 4, 5, 6]
list_6.append(7)
list_6.insert(0, 0)
print(list_6)

# 第七题
list_7 = [1, 2, 3, 4, 5, 6, 7]
list_7.reverse()
print(list_7)

# 第八题
list_8 = [1, 2, 3, 4, 5, 6, 7]
list_8.reverse()
print(list_8.index(5))

# 第九题
list_9 = [True, False, 0, 1, 2]
for i in list_9:
    print(i, list_9.count(i))
# True和1,False和0被认为是等价的

# 第十题
list_10 = [True, 1, 0, 'x', None, 'x', False, 2, True]
while list_10.count('x'):
    list_10.remove('x')
print(list_10)

# 第十一题
list_11 = [True, 1, 0, 'x', None, 'x', False, 2, True]
list_11.pop(4)
print(list_11)

# 第十二题
list_12 = [True, 1, 0, 'x', None, 'x', False, 2, True]


def remove_odd_indices(lst):
    return [item for i, item in enumerate(lst) if i % 2 == 0]


def remove_even_indices(lst):
    return [item for i, item in enumerate(lst) if i % 2 == 1]


print(remove_odd_indices(list_12))
print(remove_even_indices(list_12))

# 第十三题
list_13 = [True, 1, 0, 'x', None, 'x', False, 2, True]
list_13.clear()
print(list_13)

# 第十四题
list_14_1 = [3, 0, 8, 5, 7]
list_14_1.sort()
print(list_14_1)

list_14_2 = [3, 0, 8, 5, 7]
list_14_2.sort(reverse=True)
print(list_14_2)

# 第十五题
list_15 = [3, 0, 8, 5, 7]
print([1 if x > 5 else 0 for x in list_15])

# 第十六题
list_16 = ['x', 'y', 'z']
for i in range(len(list_16)):
    print(i, list_16[i])

# 第十七题
list_17 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list_17_odd = [x for x in list_17 if x % 2 == 1]
list_17_even = [x for x in list_17 if x % 2 == 0]
print(list_17_odd)
print(list_17_even)

# 第十八题
list_18 = [[6, 5], [3, 7], [2, 8]]
print(sorted(list_18))

# 第十九题
list_19 = [1, 4, 7, 2, 5, 8]
list_19[3:3] = ['x', 'y', 'z']
print(list_19)

# 第二十题
list_20 = [x for x in range(5, 50)]
print(list_20)

# 第二十二题
list_22_1 = ['x', 'y', 'z']
list_22_2 = [1, 2, 3]
list_22 = list(zip(list_22_1, list_22_2))
print(list_22)

# 第二十三题
dict_23 = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
print(list(dict_23.keys()))

# 第二十四题
dict_24 = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
print(list(dict_24.values()))

# 第二十五题
dict_25 = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
print(list(zip(dict_25.keys(), dict_25.values())))

# 第二十六题
dict_26 = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
dict_26['David'] = 19
dict_26['Cecil'] = 17
print(dict_26)

# 第二十七题
dict_27 = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
del dict_27['Beth']
print(dict_27)
dict_27.clear()
print(dict_27)

# 第二十八题
dict_28 = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
if 'David' in dict_28:
    print('David is in dict')
else:
    print('David is not in dict')
if 'Alice' in dict_28:
    print('Alice is in dict')
else:
    print('Alice is not in dict')

# 第二十九题
dict_29 = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
for i in dict_29:
    print(i, dict_29[i])
# 第三十一题
list_31 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
dict_31 = {letter: 0 for letter in list_31}
print(dict_31)



