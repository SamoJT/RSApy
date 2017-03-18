import random
import collections
import sys
import time
import re

def gcd(a,b):
	while b != 0:
		a, b = b, a%b
	return a

def coprime(a,b):
	return gcd(a,b) == 1

def is_prime(a):
	return all(a % i for i in range(2, a))

def PubPrivGen(p,q,timeout):
	n = p*q 
	phiN = (p-1)*(q-1)
	eList = []
	print("Working, be patient!\n")
	for e in range(1,phiN+1):
		if e > 1 and e < phiN:
			if coprime(e,phiN) == True:
				eList.append(e)
			else:
				continue
		else:
			continue
	valDic = {"A":0,"B":0,"C":0,"D":0}
	cout = 0
	for i in range(4):
		#I expect i can be written more pythonic, was having trouble.
		if cout == 0:
			valDic["A"] = random.choice(eList)
			cout+=1
		elif cout == 1:
			valDic["B"] = random.choice(eList)
			cout+=1
		elif cout == 2:
			valDic["C"] = random.choice(eList)
			cout+=1
		else:
			valDic["D"] = eList[-1]
			eList = []
	#print(valDic)
	print("A: %d \nB: %d \nC: %d \nD: %d" %(valDic["A"],valDic["B"],valDic["C"],valDic["D"]))
	inp = input("Enter a letter value from this list: ")
	while inp.upper() not in valDic:
		inp = input("Error value not in list. Enter a letter value from this list: ")
	e = valDic[inp.upper()]
	#print(str(inp) + str(e))
	count = 0
	val = 1
	print("Working! Be patient.")
	start_time = time.time()
	while count != val:
		dTemp = random.randrange(val)
		#print((dTemp*e)%phiN) #DEBUG
		if (dTemp*e)%phiN == 1:
			d = dTemp 
			break
		else:
			count += 1
			val += 1
			#print("Attempt: " + str(count) +" failed with value: " + str(dTemp)) IF ENABLED TAKES UPTO 26x AS LONG! (if not more)
			if time.time()-start_time >= timeout:
				return("Failed due to timeout of %s seconds." % (timeout))
			continue
	return("%s \nThe public key is (e,n): (%d,%d) \nThe private key is (d,n): (%d,%d)  \nDone in %s seconds on attempt no. %d. \n %s" % (
		("-"*60),e,n,d,n,str(time.time()-start_time),count,("-"*60)))

def main():
	print("----Choose primes larger than 5-----")
	print("Please note this is not optimised and the larger the prime the longer it takes to compute the keys.")
	timeout = input("Enter a timeout value for the keygen in seconds. press enter to default to 60. >> ")
	while any(c.isalpha() for c in timeout) == True:
		timeout = input("Enter a timeout value for the keygen in seconds, must be int or float. Press enter to default to 60. >> ")
	if timeout == "":
		timeout = 60
	timeout = float(timeout)
	#print(type(timeout))
	#print(timeout)

	p = int(input("Enter a secret prime number: "))
	while is_prime(p) != True:
		p = int(input("Enter a secret *PRIME* number: "))
	q = int(input("Enter another secret prime: "))
	while is_prime(q) != True:
		q = int(input("Enter another secret *PRIME*: "))
	print(PubPrivGen(p,q,timeout))

if __name__ == '__main__':
	sys.exit(main())