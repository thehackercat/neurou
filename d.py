#!/usr/bin/python
import random
M=[0 for i in  range(10)]
X=[1,2,3,4,5,6,7,8,9,10]
Y=[0,1,0,1,0,1,0,1,0,1]
st = 100
o=[0 for i in  range(10)]
def init():
	for n in range(10):
		M[n]=random.randint(0,99)
	
def active(m,n):
	o=m*n
	
	if o>st:
		return 1
	else:
		return 0

def ca():
	
	for p in range(10):
		o[p]=active(M[p], X[p])
		
def adjust():
	err = 0
	x = 0
	for n in range(10):
		if o[n]!=Y[n]:
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
			
 

 



		
		 

	 
