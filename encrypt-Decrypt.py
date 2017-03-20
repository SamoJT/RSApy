#!/usr/bin/env python3.5
import binascii
import pickle
import sys

def power(y, x, n):
    if x == 0: #base case
        return 1
    elif (x%2==0): #x even 
        return power((y*y)%n,x//2,n)%n
    else: #x odd
        return (y*power((y*y)%n,x//2,n))%n

def encrypt(msg,e,n):
	encMsg = []
	for i in msg:
		encMsg.append(power(ord(i),e,n))
	#print(encMsg)
	return(fileMk(encMsg))

def fileMk(encMsg):
	f = open("rsaEnc.txt","wb")
	pickle.dump(encMsg,f)
	f.close()
	return(print("File created. Success. Send the owner of the key the txt file."))

def fileOp():
	f = open("rsaEnc.txt","rb")
	c = pickle.load(f)
	f.close()
	return(c)

def decrypt(d,n):
	c = fileOp()
	msg = ""
	print("Be patient! May take some time.")
	for  i in c:
		tst = power(i,d,n)
		msg = msg+chr(power(i,d,n))
	return(print(msg))

def main():
	choice = input("Are you encrypting or decrypting? e or d >> ")
	if choice.upper() == "E":
		m = input("Enter a message to be encrypted. Use '.' instead of space: ")
		e = int(input("Enter the public key pt. e: "))
		n = int(input("Enter the public key pt. n: "))
		encrypt(m,e,n)
	else:
		d = int(input("Enter private key pt. d: "))
		n = int(input("Enter private key pt. n: "))
		decrypt(d,n)

if __name__ == '__main__':
	sys.exit(main())
