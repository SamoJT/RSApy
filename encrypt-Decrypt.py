#!/usr/bin/env python3.5

#Rename all the stupid fucking variables
#
#

import pickle
import sys
import binascii
import os
import re
import random

def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

def encrypt(msg,e,n):
	encMsgList = []
	encmsgPrinted = ""
	for i in msg:
		i = ord(i)
		encMsgList.append(pow(i,e,n)) #FOR TXT FILE
	one = msg.encode()
	two = int.from_bytes(one,byteorder = "big")
	two = str(two)
	#print(two)
	chunkedList = list(chunkstring(two,6))
	#print(chunkedList)
	for i in chunkedList:
		i = int(i)
		#print(i)
		a = pow(i,e,n)
		b = "{:x}".format(a)
		encmsgPrinted = (encmsgPrinted+str(b)+"/")

	#print("Send either the .txt file or the string of numbers to the recipient. \n")
	print(encmsgPrinted)
	return(fileMk(encMsgList))

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

def binToNum(binary_str):
	length = len(binary_str)
	num = 0
	for i in range(length):
	   num = num + int(binary_str[i])
	   num = num * 2
	return int(num/2)


def decrypt(d,n,m):
	msg = ""
	numStr = ""
	msgList = []
	count = 0
	move = False
	if m == None:
		c = fileOp()
		print("Be patient! May take some time.")
		for  i in c:
			msg = msg+chr(pow(i,d,n))
		return(print(msg))
	else:
		splitlist = re.split("/",m)
		splitlist = list(filter(None,splitlist))
		#print(splitlist)
		count = 1
		for i in splitlist:
			dec = int(i,16)
			unRSA = pow(dec,d,n)
			#print(unRSA)
			if len(str(unRSA)) < 6 and count < len(splitlist):
				numStr = numStr+"0"+str(unRSA)
				count += 1
			else:
				numStr = numStr+str(unRSA)
				count += 1

		num = int(numStr)
		#print(num)
		msgEn = num.to_bytes(num.bit_length(), byteorder="big")
		#print(msgEn)
		decoded = msgEn.decode()
		
		print("Your decoded message is:")
		print(decoded)
		return


		

def main():
	#TESTING
	#Pub - 65537,25060027
	#Priv - 2317825,25060027
	
	#encrypt("It finally fucking works!",65537,25060027)
	#return
	#print("DONE \n")
	#decrypt(2317825,25060027,"1339fec/16d467c/72c2aa/c8286b/118110c/122dde3/9b1020/2b9db/55d66/845c07/")

	#return
	
	############################################################################################

	choice = input("Are you encrypting or decrypting? e or d >> ")
	if choice.upper() == "E":
		m = input("Enter a message to be encrypted: ")
		e = int(input("Enter the public key pt. e: "))
		n = int(input("Enter the public key pt. n: "))
		encrypt(m,e,n)
	else:
		choice2 = input("Are you inputting the binary string (b) or using rsaEnc.txt (r)? \n")
		if choice2 == "r":
			print("Ensure the rsaEnc.txt from the sender is in the same directory. \n")
			d = int(input("Enter private key pt. d: "))
			n = int(input("Enter private key pt. n: "))
			m = None
			decrypt(d,n,m)
		else:
			m = input("Enter binary string: ")
			d = int(input("Enter private key pt. d: "))
			n = int(input("Enter private key pt. n: "))
			decrypt(d,n,m)

if __name__ == '__main__':
	sys.exit(main())



'''		
WIP to give a binary output.

		bina = bin(power(ord(i),e,n))
		strp = bina.strip("0b")
		if len(strp) != 8:
			x = 8-len(strp)
			strp = (x*"0")+strp
		encMsghex = encMsgbin+strp
	print(encMsgbin)

'''


'''
		toBytes = str.encode(str(j))
		toHexByte = binascii.hexlify(toBytes)
		toHexStr = toHexByte.decode()
		toBeAdded = int(len(toHexStr)/2)
		toBeAdded = toBeAdded-1
		randint = random.randint(97,102)
		randchr = chr(randint)
		toHexStr = toHexStr+randchr
		randHexEn = binascii.b2a_hex(os.urandom(toBeAdded))
		randHexDe = randHexEn.decode()
		toHexStr = toHexStr+randHexDe
		randint = random.randint(97,102)
		randchr = chr(randint)
		toHexStr = toHexStr+randchr
		out = out+toHexStr
		while len(out)%8 != 0 :
			randint = random.randint(97,102)
			randchr = chr(randint)
			out = out+randchr
'''
'''
		for i in m:
			if move == True:
				count += 1
				if count == 15:
					move = False
					count = 0
					continue
				continue
			if i.isalpha() == True:
				msgList.append(msg)
				msg = ""
				move = True
			else:
				msg = msg+i
				continue
		if '' in msgList:
			msgList.remove('')
		for i in msgList:
			unhexed = binascii.unhexlify(i)
			unhexedDec = unhexed.decode()
			unhexedDec = int(unhexedDec)
			msg = msg+chr(power(unhexedDec,d,n))
'''