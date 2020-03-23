print('------------------------')

print('第二十六题：字符串判断')
# 测试实例一
print("测试实例一")
str = "runoob.com"
print(str.isalnum()) # 判断所有字符都是数字或者字母
print(str.isalpha()) # 判断所有字符都是字母
print(str.isdigit()) # 判断所有字符都是数字
print(str.islower()) # 判断所有字符都是小写
print(str.isupper()) # 判断所有字符都是大写
print(str.istitle()) # 判断所有单词都是首字母大写，像标题
print(str.isspace()) # 判断所有字符都是空白字符、\t、\n、\r

print("------------------------")

# 测试实例二
print("测试实例二")
str = "runoob"
print(str.isalnum())
print(str.isalpha())
print(str.isdigit())
print(str.islower())
print(str.isupper())
print(str.istitle())
print(str.isspace())

print('------------------------')

print('第二十七题：字符串大小写转换')

str = "www.runoob.com"
print(str.upper())          # 把所有字符中的小写字母转换成大写字母
print(str.lower())          # 把所有字符中的大写字母转换成小写字母
print(str.capitalize())     # 把第一个字母转化为大写字母，其余小写
print(str.title())          # 把每个单词的第一个字母转化为大写，其余小写

print('------------------------')

print('第二十八题：计算每个月天数')
n = int(input("输入年份"))
m = int(input("输入月份"))
import calendar
monthRange = calendar.monthrange(n,m)
print(monthRange)

print('------------------------')

print('第二十九题：计算昨天日期')
# 引入 datetime 模块
import datetime

def getYesterday():
    yesterday = datetime.date.today() + datetime.timedelta(-1)
    return yesterday
# 输出
print(getYesterday())

