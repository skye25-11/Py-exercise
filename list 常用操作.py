li = ["a", "b", "c", "z", "e"]
#list 负数索引
print('定义和复数索引')
print(li[1])
print(li[-3])
print(li[1:3])
print(li[1:-1])
print(li[0:3])

print('------------------------')
#list 增加元素
print('添加元素')
li.append("new")
print(li)
li.insert(2, "new")#位置
print(li)
li.extend(["two", "elements"])#保留前元素
print(li)

print('------------------------')
#list 搜索
print('搜索')
print(li.index('b'))
print("new" in li)#判断元素是否存在

print('------------------------')
#list 删除元素
li.remove('z')
print(li,'删除z')
li.remove("new")    # 删除首次出现的一个值
print(li,'第二个 new 未删除')
print(li,'使用pop前')# pop 会做两件事: 删除 list 的最后一个元素, 然后返回删除元素的值。
print(li.pop())

print('------------------------')
#list 运算符
print('运算符')
li =['a', 'b', 'mpilgrim']
li = li + ['example', 'new']
li += ['two']
print(li)
li = [1, 2] * 3
print(li)

print('------------------------')
#list 使用join链接list成为字符串
#join 只能用于元素是字符串的 list; 它不进行任何的类型强制转换。
#连接一个存在一个或多个非字符串元素的 list 将引发一个异常。
print('使用join链接list成为字符串')
params = {"aa1":"AA1", "bb1":"BB1", "cc1":"CC1", "dd1":"DD1"}
a=["%s=%s" % (k, v) for k, v in params.items()]
b=";".join(["%s=%s" % (k, v) for k, v in params.items()])
print(a)
print(b)

print('------------------------')
#list 分割字符串
#split 与 join 正好相反, 它将一个字符串分割成多元素 list。
#注意, 分隔符 (";") 被完全去掉了, 它没有在返回的 list 中的任意元素中出现。
#split 接受一个可选的第二个参数, 它是要分割的次数。
print('分割字符串')
li = ['aa1=AA1', 'bb1=BB1', 'cc1=CC1', 'dd1=DD1']
s = ";".join(li)
print(s)
a = s.split(";")
print(a)
b = s.split(";", 1)
print(b)

print('------------------------')
#list 的映射解析
print('映射')
li = [1, 9, 8, 4]
a = [elem*2 for elem in li]
print(a)
li = [elem*2 for elem in li]
print(li)

print('------------------------')
#dictionary 中的解析
params = {"aa1":"AA1", "bb1":"BB1", "cc1":"CC1", "dd1":"DD1"}
print(params.keys())
print(params.values())
print(params.items())
a = [k for k, v in params.items()]
print(a)
b = [v for k, v in params.items()]
print(b)
c =["%s=%s" % (k, v) for k, v in params.items()]
print(c)

print('------------------------')
#list 过滤
print('过滤条件元素')
li = ["a", "aa", "aaa", "b", "c", "b", "d", "d"]
print(li)

a = [elem for elem in li if len(elem) > 1]  #len() 方法返回对象（字符、列表、元组等）长度或项目个数
b = [elem for elem in li if elem != "b"]
c = [elem for elem in li if li.count(elem) == 1]#count() 方法用于统计字符串里某个字符出现的次数。
print(a,'返回对象长度大于1的过滤')
print(b,'过滤掉b')
print(c,'过滤掉出现2次的')

