import binascii
import pickle
import sys

def encrypt(msg,e,n):
	alpha = ["A","B","C","D","E",
	"F","G","H","I","J","K","L",
	"M","N","O","P","Q","R","S",
	"T","U","V","W","X","Y","Z","."]
	msgList = list(msg.upper())
	encMsg = []
	for i in msgList:
		ind = alpha.index(i)
		c0 = ind**e
		c1 = c0%n
		#print(c1)
		encMsg.append(c1)
	return(fileMk(encMsg))

def fileMk(encMsg):
	f = open("rsaEnc.txt","wb")
	pickle.dump(encMsg,f)
	f.close()
	return(print("File creted. Success. Send the owner of the key the txt file."))

def fileOp():
	f = open("rsaEnc.txt","rb")
	c = pickle.load(f)
	f.close()
	return(c)

def decrypt(d,n):
	alpha = ["A","B","C","D","E",
	"F","G","H","I","J","K","L",
	"M","N","O","P","Q","R","S",
	"T","U","V","W","X","Y","Z","."]
	c = fileOp()
	msg = ""
	print("Be patient! May take some time.")
	for  i in c:
		m0 = i**d
		m1 = m0%n
		msg = msg+alpha[m1]
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
