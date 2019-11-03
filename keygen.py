import collections
import sys
import time
'''
A python 3.6+ RSA key generator. Used in conjunction with encrypt-Decrypt
to create encoded hex strings or .txt files which can be sent to the desired
recipient.
'''

def is_prime(a):
	return all(a % i for i in range(2, a))

def PubPrivGen(p,q,timeout,gui):
	n = p*q
	if len(str(n)) < 7:
		print("The value of n was less than 6 digits long.")
		return(main())
	phiN = (p-1)*(q-1)
	e = 65537
	val = 2
	print("Working! Be patient.")
	start_time = time.time()

	while (val*e)%phiN != 1:
		val += 1
		if time.time()-start_time >= timeout:
			return(f"Failed due to timeout of {timeout} seconds.")

	if gui == True:
		return(e,n,d)
	else:
		return(f"{'-'*60}\nThe public key is (e,n): ({e},{n})\nThe private key is (d,n): ({val},{n})\nDone in {str(time.time()-start_time)} on attempt no. {count}\n{'-'*60}")

def main():	
	gui = False
	print("----Choose primes larger than 5000----")
	timeout = input("Enter a timeout value for the keygen in seconds. [ENTER] to default to 60:  ")
	while any(c.isalpha() for c in timeout) == True:
		timeout = input("Enter a timeout value for the keygen in seconds, must be int or float. Press enter to default to 60. >> ")
	if timeout == "":
		timeout = 60
	timeout = float(timeout)

	p = False
	while True:
		if not p:	
			p = int(input("Enter a secret prime number: "))
			if is_prime(p) == False:
				print("Not a prime. Please try another number")
				p = False
				continue

		q = int(input("Enter another secret prime: "))
		if is_prime(q) == False:
			print("Not a prime. Please try another number")
			continue
		break

	print(PubPrivGen(p,q,timeout,gui))

if __name__ == '__main__':
	sys.exit(main())