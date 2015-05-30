#!/usr/bin/python
# -*- coding: utf-8 -*
#然后我试试能不能扩张到100之内的奇偶数判定，如果可以，那就可以扩张到无限大的数的奇偶判定
import random
M = [0 for i in range(100)]

X = range(1,101)

Y = []
for x in range(100):
	if x%2 == 0:
		Y.append(0)
	else:
		Y.append(1)


st = 1000

o=[0 for i in range(100)]

def init():
	for n in range(100):
		M[n] = random.randint(0,999)

def active(m,n):
	o=m*n

	if o>st:
		return 1
	else:
		return 0

def ca():

	for p in range(100):
		o[p] = active(M[p], X[p])

def adjust():
	err = 0
	x = 0
	for n in range(100):
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
	print 'Please input your number between 1-100'
	print '\n'

	while(1):


		a=raw_input()
		a=int(a)
		if a>100 or a<0:
			break

		test(a)
		print '\n'


main()
