print('------------------------')
'''30 个人在一条船上，超载，需要 15 人下船。
于是人们排成一队，排队的位置即为他们的编号。
报数，从 1 开始，数到 9 的人下船。
如此循环，直到船上仅剩 15 人为止，问都有哪些编号的人下船了呢？'''
print('约瑟夫生者死者小游戏')
people={}
for x in range(1,31):
    people[x]=1
print('第三十一题：船上共有30人')
check=0
i=1
j=0
while i<=31:
    if i == 31:
        i=1
    elif j == 15:
        break
    else:
        if people[i] == 0:
            i+=1
            continue
        else:
            check+=1
            if check == 9:
                people[i]=0
                check = 0
                print("{}号下船了".format(i))
                j+=1
            else:
                i+=1
                continue

print('------------------------')
'''A、B、C、D、E 五人在某天夜里合伙去捕鱼，到第二天凌晨时都疲惫不堪，于是各自找地方睡觉。
日上三杆，A 第一个醒来，他将鱼分为五份，把多余的一条鱼扔掉，拿走自己的一份。
B 第二个醒来，也将鱼分为五份，把多余的一条鱼扔掉拿走自己的一份。 。
C、D、E依次醒来，也按同样的方法拿鱼。
问他们台伙至少捕了多少条鱼?'''
print('第三十二题：五人分鱼')
def main():
    fish = 1
    while True:
        total, enough = fish, True
        for _ in range(5):
            if (total - 1) % 5 == 0:
                total = (total - 1)  //  5 * 4
            else:
                enough = False
                break
        if enough:
            print(f'总共有{fish}条鱼')
            break
        fish += 1
if __name__ == '__main__':
    main()

print('------------------------')
print('第三十三题：计算n个自然数的立方和')
# 定义立方和的函数
def sumOfSeries(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * i * i
    return sum
# 调用函数
n =int (input('请输入数字 n '))
print(sumOfSeries(n))

print('------------------------')
print('第三十四题： 计算数组元素之和')
print('方法一')
# 定义函数，arr 为数组，n 为数组长度，可作为备用参数，这里没有用到
def _sum(arr, n):
    # 使用内置的 sum 函数计算
    return (sum(arr))
# 调用函数
arr = []
# 数组元素
arr = [12, 3, 4, 15]
# 计算数组元素的长度
n = len(arr)
ans = _sum(arr, n)
# 输出结果
print('数组元素之和为', ans)
print('数组元素的个数',n)

print('方法二')
list=[12,3,4,15]
sum=0
for i in range(0,len(list)):
    sum+=list[i]
print(sum)
print('方法三')
from functools import reduce #reduce函数对元素累计
list=[12,3,4,15]
print(reduce(lambda x,y:x+y,list))

print('------------------------')
print('第三十五题： 实现秒表功能')
import time
print('按下回车开始计时，按下 Ctrl + C 停止计时')
input()
print('Started.')
startTime = time.time()
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        laptime = round((time.time() - lastTime), 2)
        totalTime = round((time.time() - startTime), 2)
        print('Lap: %s; 间隔时间: %s; 记时时间: %s' % (lapNum, laptime, totalTime), end=' ')
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    print('\n结束')
    input('click any key to exit')