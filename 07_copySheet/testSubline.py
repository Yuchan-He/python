# -*- coding: utf-8 -*-
"""
このモジュールの説明
"""
a = 98
b = 2
c = a + b
print(c)

# 调用函数划线
def myLine():
	print('-'*20)

i = 1
while(i<5):
	i=i+1
	myLine()

# 把局部变量变为全局变量的方法 globle
a = 100
def testA():
    print(a)

def testB():
    a = 200
    print(a)

def testC():
	# error global a = 100 
    global a
    a = 400
    print(a)



testA()
testB() 

testC()
testA()

# 各种数据的类型
"""
1.string
2.list 列表 [ ]  数组
3.tuple 元组 （ ）不能修改的数组，要修改，可在元组中添加列表 （ A，B,[C,d ] ）
4.set  集合 { } 内部有重复数组，输出没有重复数字的数组
5.dictionar 字典  { } 键值对形式的数组

"""
a = 'string'
print(type(a)) # 1.string

b = [1,'tom',3]
c = [1]
d = [1,]
print(type(b))
print(type(c)) 
print(type(d))# 2.list

e = ('test',3)
f = ('test')
g = ('test',)
print(type(e)) 
print(type(f)) 
print(type(g))# 3.tuple

h = {10,20,10}
print(type(h)) 
print(h) #4.set 

i = {'name':'tom','age':34}
print(type(i))
print(i)

# 递归算法
"""
1.特点：自己调用自己 + 必须要有一个出口
2.例：求3以内数字的累加合 3+2+1 = 6
递归算法如下
6=3+2以内数字的累加
2=2+1以内数字的累加
1=1以内数字的累加
1以内数字的累加 = 1， 已经不能往下，这就是递归函数的出口

"""

def sum_numbers(num):
	# 如果是1，则直接返回1，因为是出口
	if(num == 1):
		return 1
	# 如果不是1，则重复执行累加并返回结果
	return num + sum_numbers(num-1)

sum_result = sum_numbers(3)
print(sum_result)