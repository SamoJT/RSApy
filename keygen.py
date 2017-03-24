#!/usr/bin/env python3.5
import collections
import sys
import time
from math import gcd as bltin_gcd
'''
A python 3.5+ RSA key generator. Used in conjunction with encrypt-Decrypt
to create encoded hex strings or .txt files which can be sent to the desired
recipient.
'''
def coprime(a, b):
    return bltin_gcd(a, b) == 1

def is_prime(a):
	return all(a % i for i in range(2, a))

def PubPrivGen(p,q,timeout):
	n = p*q
	if len(str(n)) < 7:
		print("The value of n was less than 6.")
		return(main())
	phiN = (p-1)*(q-1)
	e = 65537
	count = 0
	val = 1
	print("Working! Be patient.")
	start_time = time.time()
	while count != val:
		dTemp = val
		if (dTemp*e)%phiN == 1:
			d = dTemp
			break
		else:
			count += 1
			val += 1
			if time.time()-start_time >= timeout:
				return("Failed due to timeout of %s seconds." % (timeout))
			continue
	return("%s \nThe public key is (e,n): (%d,%d) \nThe private key is (d,n): (%d,%d)  \nDone in %s seconds on attempt no. %d. \n %s" % (
		("-"*60),e,n,d,n,str(time.time()-start_time),count,("-"*60)))

def main():
	print("----Choose primes larger than 5000----")
	timeout = input("Enter a timeout value for the keygen in seconds. [ENTER] to default to 60:  ")
	while any(c.isalpha() for c in timeout) == True:
		timeout = input("Enter a timeout value for the keygen in seconds, must be int or float. Press enter to default to 60. >> ")
	if timeout == "":
		timeout = 60
	timeout = float(timeout)

	p = int(input("Enter a secret prime number: "))
	while is_prime(p) != True:
		p = int(input("Enter a secret *PRIME* number: "))
	q = int(input("Enter another secret prime: "))
	while is_prime(q) != True:
		q = int(input("Enter another secret *PRIME*: "))
	print(PubPrivGen(p,q,timeout))

if __name__ == '__main__':
	sys.exit(main())