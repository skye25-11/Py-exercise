print('------------------------------')

print('第二十一题：最大公约数算法')

# 定义一个函数
def hcf(x, y):
    """该函数返回两个数的最大公约数"""

    # 获取最小值
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i

    return hcf


# 用户输入两个数字
num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))

print(num1, "和", num2, "的最大公约数为", hcf(num1, num2))

print('------------------------------')

print('第二十二题：最小公倍数算法')

# 定义函数
def lcm(x, y):
    #  获取最大的数
    if x > y:
        greater = x
    else:
        greater = y

    while (True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm


# 获取用户输入
num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))

print(num1, "和", num2, "的最小公倍数为", lcm(num1, num2))

print('------------------------------')

print('第二十三题：生成日历')
# 引入日历模块
import calendar

# 输入指定年月
yy = int(input("输入年份: "))
mm = int(input("输入月份: "))
calendar.setfirstweekday(firstweekday=6)#设置第一天是星期天

# 显示日历
print(calendar.month(yy,mm))

print('------------------------------')

print('第二十四题：使用递归斐波那契数列')

def recur_fibo(n):
    """递归函数
    输出斐波那契数列"""
    if n <= 1:
        return n
    else:
        return (recur_fibo(n - 1) + recur_fibo(n - 2))


# 获取用户输入
nterms = int(input("您要输出几项? "))

# 检查输入的数字是否正确
if nterms <= 0:
    print("输入正数")
else:
    print("斐波那契数列:")
    for i in range(nterms):
        print(recur_fibo(i))

print('------------------------------')

print('第二十五题：文件IO')

n = input("输入文本内容")
with open(r'C:\Users\Administrator\Desktop\s.txt','wt') as fileout:
    fileout.write(n)
with open(r'C:\Users\Administrator\Desktop\s.txt','rt') as filein:
    print(filein.readline())