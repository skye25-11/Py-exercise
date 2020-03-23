print('------------------------------')

print('第十一题：判断奇偶数')

while True:
    try:
        num=int(input('输入一个整数：')) #判断输入是否为整数
    except ValueError: #不是纯数字需要重新输入
        print("输入的不是整数！")
        continue
    if num%2==0:
        print('偶数')
    else:
        print('奇数')
    break

print('------------------------------')

print('第十二题：判断闰平年')
#Python 的 calendar 库中已经封装好了一个方法 isleap() 来实现这个判断是否为闰年
#import calendar
#>>> print(calendar.isleap(2000))
#True
#>>> print(calendar.isleap(1900))
#False
import calendar

year = int(input("请输入年份："))
check_year=calendar.isleap(year)
if check_year == True:
    print ("闰年")
else:
    print ("平年")

print('------------------------------')

print('第十三题：获取最大值函数')

# 最简单的
print(max(1, 2))
print(max('a', 'o'))

# 也可以对列表和元组使用
print(max([1, 8]))
print(max((1, 2)))

# 更多实例
print("80, 100, 1000 最大值为: ", max(80, 100, 1000))
print("-20, 100, 400最大值为: ", max(-20, 100, 400))
print("-80, -20, -10最大值为: ", max(-80, -20, -10))
print("0, 100, -400最大值为:", max(0, 100, -400))

print('------------------------------')

print('第十四题：质数判断')

# Python 程序用于检测用户输入的数字是否为质数

# 用户输入数字
num = int(input("请输入一个数字: "))

# 质数大于 1
if num > 1:
    # 查看因子
    for i in range(2, num):#在某个区间
        if (num % i) == 0:
            print(num, "不是质数")
            print(i, "乘于", num // i, "是", num)
            break
    else:
        print(num, "是质数")

# 如果输入的数字小于或等于 1，不是质数
else:
    print(num, "不是质数")

print('------------------------------')

print('第十五题：输出指定范围内的素数')

lower = int(input("输入区间最小值: "))
upper = int(input("输入区间最大值: "))

for num in range(lower, upper + 1):
    # 素数大于 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)