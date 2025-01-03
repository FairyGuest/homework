# 1、练习深copy与浅copy
# 2、练习上课匹配单个字符，多个字符，匹配分组的正则表达式案例
# 3、练习上课的search，findall,sub等案例
import copy
import re

# 第一题
# 浅copy
original_list = [1, [2, 3], (4, 5)]
shallow_copy = copy.copy(original_list)  # 虽然隔开了，但是内部类似于指针的结构仍一致，像是一个新的结构，但是结构内容一致
print('original:', original_list, 'id:', id(original_list))
print('shallow:', shallow_copy, 'id:', id(shallow_copy))

original_list[1][0] = 'X'
print('After modification:')
print('original:', original_list, 'id:', id(original_list))
print('shallow:', shallow_copy, 'id:', id(shallow_copy))

# 深copy
original_list = [1, [2, 3], (4, 5)]
deep_copy = copy.deepcopy(original_list)  # 这是开辟了一个全新的空间，所有嵌套内容都被递归复制，创建了完全独立的副本
print('original:', original_list, 'id:', id(original_list))
print('deep_copy:', deep_copy, 'id:', id(deep_copy))

original_list[1][0] = 'X'
print('After modification:')
print('original:', original_list, 'id:', id(original_list))
print('deep_copy:', deep_copy, 'id:', id(deep_copy))

# 第二题
# 单个字符
ret = re.match('t.o', 'too')
print(ret.group())

ret = re.match('[hH]', 'Hello world')
print(ret.group())
# 多个字符
ret = re.finditer(r'\d+', 'I have 123 apples and 45 oranges')
next(ret)
second_ret = next(ret)
print(second_ret.group())

ret = re.match('[1-9]?\d', '33')
print(ret.group())

ret = re.match('[a-zA-Z0-9_]{8,20}', '23123kjhkajdhf_82sdwesd3w4213_')
print(ret.group())

# 匹配开头和结尾
email_list = ["xiaoWang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang@qq.com"]
for email in email_list:
    ret = re.match(r'\w{4,20}@163.com$', email)
    if ret:
        print(f'{ret.group()}是正确邮箱地址')
    else:
        print(f'{email}不正确')

text_list = ['Hello world', 'Hello python', 'hello World', 'adsodfiw']
for text in text_list:
    ret = re.match(r'^Hello', text)
    if ret:
        print(f'{ret.group()}是正确字符串')
    else:
        print(f'{text}不正确')

# 匹配分组
ret = re.findall(r'(\d{4})/([01]{0,1}[0-9]{1})/([0-3]{0,1}[0-9]{1})', 'Today is 2025/1/3, and tomorrow is 2025/01/04')
print(ret)  # 年月日都分开了，并且组成了元组

# 第三题
ret = re.search(r'\d{2}',' I take 22 xxx to 33 xxx')
print(ret.group())

ret = re.findall(r'\d{2}',' I take 22 xxx to 33 xxx')
print(ret)

ret = re.sub(r'\d+', '100', 'python-100000000')
print(ret)

ret = re.sub(r'apple', 'orange', 'apple apple orange orange', count=1)
print(ret)
