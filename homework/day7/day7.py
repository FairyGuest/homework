# 1.完成包的使用（与上课一致）
# 2.完成文件的文本模式的读，写（与上课一致）
# 3.完成目录的listdir，getcwd,chdir的使用（与上课一致）
# 4.完成python的传参练习（与上课一致）
#
# 代码编写与上课一致即可
#
# 难度作业：
# 5、完成普通文件文件的seek，二进制文件的seek（代码编写与上课一致即可）
# 6、完成目录深度优先遍历（代码编写与上课一致即可）
import os

# 第一题
import module1

module1.test_func()
test_class = module1.TestClass()
test_class.test_func()

# 第二题+第五题
# read
fd = open('test.txt', 'r', encoding='utf-8')
print(fd.read())
fd.seek(0, 0)  # 回到文件开头
print(fd.readlines())
fd.close()
# write
fd2 = open('test1.txt', 'w', encoding='utf-8')
fd2.write('hello world!')
fd2.close()
# a模式
fd3 = open('test2.txt', 'a', encoding='utf-8')
fd3.write('hello world!')
fd3.close()

# r+模式
fd4 = open('test.txt', 'r+', encoding='utf-8')
fd4.read()
fd4.write('end of file')
fd4.close()

# 第三题
file_list = os.listdir('.')
print(file_list)
print(os.getcwd())
os.chdir('dir1')
fd_3_1 = open('test.txt', 'w', encoding='utf-8')
fd_3_1.write('hello world!')
fd_3_1.close()

# 第四题

import sys


def write_hello(file_path):
    file_descriptor = open(file_path, 'w+', encoding='utf-8')
    file_descriptor.write('hello world!')
    file_descriptor.close()


write_hello(sys.argv[1])


def scan_dir(current_path, width):
    """
    深度优先遍历
    :param current_path:
    :return:
    """
    file_list = os.listdir(current_path)  # 得到当前文件夹下的所有文件
    for file in file_list:
        print(' ' * width, file)  # 打印文件名,width代表多少个空格
        new_path = current_path + '/' + file  # 把当前路径和文件名拼接到一起
        if os.path.isdir(new_path):
            scan_dir(new_path, width + 4)


scan_dir('..', 0)
