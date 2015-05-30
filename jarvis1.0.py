#!/usr/bin/python
# -*- coding: utf-8 -*
import random
#调教列表M
M = [0 for i in range(10)]
#训练列表X
X = [1,2,3,4,5,6,7,8,9,10]
#奇偶数判定列表，0为奇数，1为偶数1
Y = [0,1,0,1,0,1,0,1,0,1]
#训练次数阙值,st越大训练次数越多
st = 100

o=[0 for i in range(10)]

#为M列表赋值<0-99>随机数
def init():
	for n in range(10):
		M[n] = random.randint(0,99)

#训练的奇偶判定算法
def active(m,n):
	o=m*n

	if o>st:
		return 1
	else:
		return 0

#训练过程：通过随机数列表M与X列表相乘后通过训练算法active()
#         与Y列表比较筛选出列表中的异常索引号，
# 		  再通过adjust()对异常索引号对应的列表元素进行递减或递增，
#		  (增减值为X列表中异常索引号对应的值)
#		  得到调教完的列表M，使ca()返回的o列表 == Y列表
#		  在test()中，输入的奇偶数值即索引号，通过查询o列表中索引号对应的01值来判定奇偶
def ca():

	for p in range(100):
		o[p] = active(M[p], X[p])

def adjust():
	err = 0
	x = 0
	for n in range(10):
		if o[n]!= Y[n]:
			err+=1
			if 0==o[n]:
				M[n]+=X[n]
			else:
				M[n]-=X[n]
		print M
	return err

def test(a):
	if(active(M[a-1], X[a-1])):
		print "%d is an even number.Sir"%a
	else:
		print "%d is an odd number.Sir"%a



def main():
	n = 0
	init()
	err =0
	print "This is zhou I'm going to train my one neuron.Sir"
	print '\n'
	while(1):
		n+=1
		ca()

	 	err = adjust()
		if 0>=err:
			break

	print "Training finished by %d times. Sir "%n
	print 'Now you can test my neurou.Sir'
	print '\n'
	print 'Please input your number between 1-10'
	print '\n'

	while(1):


		a=raw_input()
		a=int(a)
		if a>10 or a<0:
			break

		test(a)
		print '\n'


main()
