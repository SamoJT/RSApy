#!/usr/bin/env python3.5
import pickle
import sys
import re
'''
A python 3.0+ tool for encrypting and/or decrypting messages
using RSA and a little formatting.
Note: It is by no means perfect and may run into a unicode error,
I found it to occur when the sum of the primes was too low.
'''

def chunkstring(string, length):
	#
    return (string[0+i:length+i] for i in range(0, len(string), length))

def fileMk(encMsg):
	f = open("rsaEnc.txt","wb")
	pickle.dump(encMsg,f)
	f.close()
	return(print("File created sucessfully! Send the owner of the key the txt file."))

def fileOp():
	f = open("rsaEnc.txt","rb")
	enMsgTxt = pickle.load(f)
	f.close()
	return(enMsgTxt)

def encrypt(msg,e,n):
	enMsgList = []
	enMsgPrint = ""
	for i in msg: #To create a list used for the txt file.
		i = ord(i)
		enMsgList.append(pow(i,e,n))
	msgBytes = msg.encode()
	msgInt = int.from_bytes(msgBytes,byteorder = "big")
	msgInt = str(msgInt)
	chunkedList = list(chunkstring(msgInt,6))
	for i in chunkedList:
		i = int(i)
		rsa = pow(i,e,n)
		hexed = "{:x}".format(rsa)
		enMsgPrint = (enMsgPrint+str(hexed)+"l")
	print("Done! Send either the .txt file or the string of numbers to the recipient. \n")
	print(enMsgPrint)
	return(fileMk(enMsgList))

def decrypt(d,n,enMsg):
	deMsg = ""
	numStr = ""
	msgList = []
	count = 0
	move = False
	if enMsg == None:
		enMsgTxt = fileOp()
		print("\nBe patient! May take some time.")
		for  i in enMsgTxt:
			deMsg = deMsg+chr(pow(i,d,n))
		return(print("%s Your decoded message is %s \n %s \n%s"%("-"*24,"-"*23,deMsg,"-"*72)))
	else:
		splitEnMsg = re.split("l",enMsg)
		splitEnMsg = list(filter(None,splitEnMsg))
		count = 1
		for i in splitEnMsg:
			dec = int(i,16)
			unRSA = pow(dec,d,n)
			if len(str(unRSA)) < 6 and count < len(splitEnMsg):
				numStr = numStr+"0"+str(unRSA)
				count += 1
			else:
				numStr = numStr+str(unRSA)
				count += 1
		msgInt = int(numStr)
		msgBytes = msgInt.to_bytes(msgInt.bit_length(), byteorder="big")
		decoded = msgBytes.decode()
		return(print("%s Your decoded message is %s \n %s \n%s"%("-"*25,"-"*25,decoded,"-"*74)))

def main():
	choice = input("Are you encrypting (e) or decrypting (d)? ")
	if choice.upper() == "E":
		m = input("Enter a message to be encrypted: ")
		e = int(input("Enter the public key pt. e: "))
		n = int(input("Enter the public key pt. n: "))
		encrypt(m,e,n)
	elif choice.upper() == "D":
		choice2 = input("Are you inputting the hex string (h) or using rsaEnc.txt (r)? ")
		if choice2 == "r":
			print("Ensure the rsaEnc.txt from the sender is in the same directory. \n")
			d = int(input("Enter private key pt. d: "))
			n = int(input("Enter private key pt. n: "))
			m = None
			decrypt(d,n,m)
		else:
			m = input("Enter hex string: ")
			d = int(input("Enter private key pt. d: "))
			n = int(input("Enter private key pt. n: "))
			decrypt(d,n,m)
	else:
		main()

if __name__ == '__main__':
	sys.exit(main())