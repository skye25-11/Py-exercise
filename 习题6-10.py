print('------------------------------')
print('第六题：随机数')
# 导入 random(随机数) 模块
import random

print(random.randint(0, float(100)))

print('------------------------------')

print("第七题：摄氏温度转华氏温度")
# 用户输入摄氏温度
a= float(input('摄氏度转华氏度输入 1 反之按 0'))
if a==1 :
    celsius = float(input('输入摄氏温度: '))
    # 计算华氏温度
    fahrenheit = (celsius * 1.8) + 32
    print('%0.1f 摄氏温度转为华氏温度为 %0.1f ' % (celsius, fahrenheit))
else :
    fahrenheit = float(input('输入华氏温度: '))
    # 计算摄氏温度
    celsius = (fahrenheit - 32) / 1.8
    print('%0.1f 华氏温度转为摄氏温度为 %0.1f ' % (fahrenheit, celsius))

print('------------------------------')

print('第八题：交换变量')
# 用户输入
x = input('输入 x 值: ')
y = input('输入 y 值: ')

# 不使用临时变量
x, y = y, x

print('交换后 x 的值为: {}'.format(x))
print('交换后 y 的值为: {}'.format(y))

print('------------------------------')

print('第九题：if语句')
# 内嵌 if 语句
while True:
    try:
        num=float(input('请输入一个数字：'))
        if num==0:
            print('输入的数字是零')
        elif num>0:
            print('输入的数字是正数')
        else:
            print('输入的数字是负数')
        break
    except ValueError:
        print('输入无效，需要输入一个数字')

print('------------------------------')

print('第十题：判断字符串是否为数字')
def is_number(s):
    try:  # 如果能运行float(s)语句，返回True（字符串s是浮点数）
        float(s)
        return True
    except ValueError:  # ValueError为Python的一种标准异常，表示"传入无效的参数"
        pass  # 如果引发了ValueError这种异常，不做任何事情（pass：不做任何事情，一般用做占位语句）
    try:
        import unicodedata  # 处理ASCii码的包
        for i in s:
            unicodedata.numeric(i)  # 把一个表示数字的字符串转换为浮点数返回的函数
            #return True
        return True
    except (TypeError, ValueError):
        pass
    return False


# 测试字符串和数字
print(is_number('foo'))  # False
print(is_number('1'))  # True
print(is_number('1.3'))  # True
print(is_number('-1.37'))  # True
print(is_number('1e3'))  # True

# 测试 Unicode
# 阿拉伯语 5
print(is_number('٥'))  # True
# 泰语 2
print(is_number('๒'))  # True
# 中文数字
print(is_number('四'))  # True
# 版权号
print(is_number('©'))  # False

