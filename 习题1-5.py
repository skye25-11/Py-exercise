print('------------------------------')
print("第一题：求和");
num1=input("输入第一个数字");
num2=input("输入第二个数字");
sum=float(num1)+float(num2);
print('数字 {0} 和 {1} 相加结果为： {2}'.format(num1, num2, sum))

print('------------------------------')

print("第二题：求平方根");
num = float(input('请输入一个数字： '))
num_sqrt = num ** 0.5  #**为求幂函数
print(' %0.5f 的平方根为 %0.5f'%(num ,num_sqrt))

print('------------------------------')

print("第三题：求平方根");
# 二次方程式 ax**2 + bx + c = 0
# a、b、c 用户提供，为实数，a ≠ 0
# 导入 cmath(复杂数学运算) 模块
import cmath
a = float(input('输入 a: '))
b = float(input('输入 b: '))
c = float(input('输入 c: '))
# 计算
d = (b ** 2) - (4 * a * c)
# 两种求解方式
sol1 = (-b - cmath.sqrt(d)) / (2 * a)
sol2 = (-b + cmath.sqrt(d)) / (2 * a)
print('结果为 {0} 和 {1}'.format(sol1, sol2))

print('------------------------------')

print("第四题：三角形边长求面积")
a = float(input('输入三角形第一边长: '))
b = float(input('输入三角形第二边长: '))
c = float(input('输入三角形第三边长: '))
# 计算半周长
s = (a + b + c) / 2
# 计算面积 海伦公式
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print('三角形面积为 %0.2f' % area)

print('------------------------------')

print("第五题：圆面积")
def findArea(r):
    PI = 3.142
    return PI * (r * r)
# 调用方法
print(f"圆的面积为 {findArea(10):.6f}")