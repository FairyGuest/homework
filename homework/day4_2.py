# 第三十二题
list_32 = [['a', 1], ['b', 2]]
set_32 = (('x', 3), ('y', 4))
dict_32_1 = dict(list_32)
dict_32_2 = dict(set_32)
dict_32 = {**dict_32_1, **dict_32_2}
print(dict_32)

# 第三十三题
tuple_33_1 = (1, 2)
tuple_33_2 = (3, 4)
tuple_33 = tuple(list(tuple_33_1) + list(tuple_33_2))
print(tuple_33)

# 第三十四题
coordinate = (1, 2, 3)
x, y, z = coordinate
print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")

# 第三十五题
tuple_35 = ('Alice', 'Beth', 'Cecil')
print(tuple_35.index('Cecil'))

# 第三十六题
tuple_36 = (2, 5, 3, 2, 4)
print(tuple_36.count(2))

# 第三十七题
tuple_37 = ('Alice', 'Beth', 'Cecil')
if 'Cecil' in tuple_37:
    print("Cecil is in tuple_37")
else:
    print("Cecil is not in tuple_37")

# 第三十八题
tuple_38 = (2, 5, 3, 7)
list_38 = list(tuple_38)
list_38.insert(2, 9)
print(tuple(list_38))

# 第三十九题
set_39 = set()
set_39.update(['x', 'y', 'z'])
print(set_39)

# 第四十题
set_40 = {'x', 'y', 'z'}
set_40.discard('z')
set_40.add('w')
print(set_40)

# 第四十一题
set_41_1 = {'A', 'D', 'B'}
set_41_2 = {'D', 'E', 'C'}
print(set_41_1-set_41_2)

# 第四十二题
set_42_1 = {'A', 'D', 'B'}
set_42_2 = {'D', 'E', 'C'}
print(set_42_1 | set_42_2)

# 第四十三题
set_43_1 = {'A', 'D', 'B'}
set_43_2 = {'D', 'E', 'C'}
print(set_42_1 & set_42_2)

# 第四十四题
print(set_43_1 ^ set_43_2)

# 第四十五题
if set_42_1 & set_42_2:
    print("有重复")
else:
    print("无重复")

# 第四十六题
set_46_1 = {'A', 'C'}
set_46_2 = {'D', 'C', 'E', 'A'}

if set_46_1.issubset(set_46_2):
    print("set_46_1 是 set_46_2 的子集")
else:
    print("set_46_1 不是 set_46_2 的子集")
# 第四十七题
list_47 = [1,2,5,2,3,4,5,'x',4,'x']
set_47 = set(list_47)
print(list(set_47))

# 第四十八题
str_48 = 'abCdEfg'
str_48_1 = str_48.upper()
print(str_48_1)
str_48_2 = str_48.lower()
print(str_48_2)
str_48_3 = str_48.swapcase()
print(str_48_3)
# 第四十九题
if str_48.istitle():
    print("首字母大写")
if str_48.isupper():
    print("字母全部大写")
if str_48.islower():
    print("字母全部小写")

str_1 = 'this is python'
# 第五十题
print(str_1.title())
print(str_1.capitalize())

# 第五十一题
if str_1.startswith('this') and str_1.endswith('python'):
    print("yes")
else:
    print("no")

# 第五十二题
print(str_1.count('is'))

# 第五十三题
print(str_1.find('is'))
print(str_1.rfind('is'))

# 第五十四题
print(str_1.split())

# 第五十五题
str_2 = 'blog.csdn.net/xufive/article/details/102946961'
print(str_2.split('/'))

# 第五十六题
str_3 = '2.72, 5, 7, 3.14'
list_3 = str_3.split(',')
list_3 = [eval(x) for x in list_3]
print(list_3)

# 第五十七题
str_4 = 'adS12K56'
if str_4.isdigit():
    print("全数字")
elif str_4.isalpha():
    print("全字母")
elif str_4.isalnum():
    print("全字母数字")
else:
    print("其他")

# 第五十八题
list_58 = str_1.split()
list_58[1] = 'are'
str_58 = ' '.join(list_58)
print(str_58)

# 第五十九题
str_59 = '\t python \n'
result_59 = str_59.strip()
print(result_59)

# 第六十题
strings_60 = ['ok', 'hello', 'thank you']
max_length = max([len(x) for x in strings_60])

print("左对齐:")
for s in strings_60:
    print(f"'{s:<{max_length}}'")

print("\n右对齐:")
for s in strings_60:
    print(f"'{s:>{max_length}}'")

print("\n居中对齐:")
for s in strings_60:
    print(f"'{s:^{max_length}}'")

# 第六十一题
numbers_61 = ['15', '127', '65535']
max_length = max(len(num) for num in numbers_61)

padded_numbers = [num.zfill(max_length) for num in numbers_61]

for num in padded_numbers:
    print(num)

# 第六十二题
list_62 = ['a', 'b', 'c']
str_62 = '|'.join(list_62)
print(str_62)

# 第六十三题
str_63 = 'abc'
str_63_1 = ','.join(str_63)
print(str_63_1)

# 第六十四题
phone_number = input("请输入十一位手机号")
print(f'Mobile:{phone_number[:3]} {phone_number[3:7]} {phone_number[7:]}')

# 第六十五题
year = input("年: ")
month = input("月: ")
day = input("日: ")
hour = input("时: ")
minute = input("分: ")
second = input("秒: ")
formatted_time = f"{year}-{month:0>2}-{day:0>2} {hour:0>2}:{minute:0>2}:{second:0>2}"
print(formatted_time)

# 第六十六题
float_1 = 3.1415926
float_2 = 2.7183
print("pi = %.4f, e=%.4f" % (float_1, float_2))

# 第六十七题
num_67_1 = 0.00774592
num_67_2 = 356800000
print(f"{num_67_1:.2e}, {num_67_2:.2e}")

# 第六十八题
list_68 = [0, 1, 2, 3.14, 'x', None, '', list(), {5}]
list_68_1 = [bool(x) for x in list_68]
print(list_68_1)

# 第六十九题
print(ord('a'),ord('A'))

# 第七十题
print(chr(57), chr(122))

# 第七十一题
list_71 = [3, 'a', 5.2, 4, {}, 9, []]
list_71_1 = [1 if isinstance(x, (int, float)) and x > 3 else 0 for x in list_71]
print(list_71_1)

# 第七十二题
list_72 = [[1], ['a', 'b'], [2.3, 4.5, 6.7]]
list_72_1 = [item for i in list_72 for item in i]
print(list_72_1)

# 第七十三题
keys_73 = ['a', 'b', 'c']
values_73 = [1, 2, 3]
result_73 = dict(zip(keys_73, values_73))
print(result_73)

# 第七十四题
numbers_74 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum(numbers_74))