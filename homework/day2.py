# 第二题
a = 1
b = 2.0
c = "hello world!"
l = True
print("a的值%d" % a, "a的类型是：", type(a))
print("b的值%.2f" % b, "b的类型是", type(b))
print("c的值%s" % c, "c的类型是", type(c))
print("l的值是：", l, "l的类型是", type(l))

# 第三题
d = 1234
print("d的二进制:", bin(d))
print("d的十六进制:", hex(d))
print("d的八进制", oct(d))

# 第四题
sum_ = 0
for i in range(1, 101):
    if i % 2 == 1:
        sum_ += i
print(sum_)

# 第五题
for m in range(1, 10):
    for n in range(1, m + 1):
        print("%d x %d = %d" % (n, m, n * m), end='  ')
    print()

# 第六题 解法1
k = int(input("请输入一个整数"))
j = k  # 用以进行解法2的变量
h = k  # 用以进行格式化输出的变量
count = 0
if k < 0:
    k = k & 0xFFFFFFFFFFFFFFFF  # 负数截断64位
while k:
    count += k & 1
    k = k >> 1
print("%d的二进制中1的个数为%d" % (h, count))
# 第六题 解法2
count_2 = 0
if j < 0:
    for i in range(0, 64):  # 若负数，则按照64位进行遍历
        count_2 += j & 1
        j = j >> 1
    print("%d的二进制中1的个数为%d" % (h, count_2))
else:
    while j:
        count_2 += j & 1
        j = j >> 1
    print("%d的二进制中1的个数为%d" % (h, count_2))
