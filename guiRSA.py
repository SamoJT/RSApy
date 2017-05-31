from tkinter import *
import sys
import time
from keygen import PubPrivGen
from encrypt_Decrypt import encrypt
from encrypt_Decrypt import decrypt

class Gui:

	def __init__(self,root):
		self.root = root

		##############START OF FRAME 1 - Keygen ############################################################

		self.frame1 = Frame(self.root,borderwidth=0,background='BLACK')
		self.frame1.pack(fill=BOTH,expand=True,side=TOP)
		########Everything to be in Frame 3#################
		self.frame3 = Frame(self.frame1,borderwidth=0,background='WHITE')
		self.generate = Button(self.frame3, text="Generate", command=lambda: self.onPressGen())
		self.lab1 = Label(self.frame3, text="Prime number 1 (p):")
		self.p = Entry(self.frame3)
		self.lab2 = Label(self.frame3, text="Prime number 2 (q):")
		self.q = Entry(self.frame3)
		###################################################
		########Everything being packed in Frame 3#########
		self.frame3.pack(fill=BOTH,expand=True,side=LEFT)
		self.lab1.pack()
		self.p.pack()
		self.lab2.pack()
		self.q.pack()
		self.generate.pack()
		###################################################
		########Everything to be in Frame 4#########
		self.frame4 = Frame(self.frame1,borderwidth=0,background='BROWN')
		self.labE = Label(self.frame4, text="Value for e (Public):")
		self.e = Entry(self.frame4)
		self.labN = Label(self.frame4, text="Value for n (Both):")
		self.n = Entry(self.frame4)
		self.labD = Label(self.frame4, text="Value for d (Private):")
		self.d = Entry(self.frame4)
		self.labRunSt = Label(self.frame4, text="Stopped")
		###################################################
		########Everything being packed in Frame 3#########
		self.frame4.pack(fill=BOTH,expand=True,side=RIGHT)
		self.labE.pack()
		self.e.pack()
		self.labN.pack()
		self.n.pack()
		self.labD.pack()
		self.d.pack()
		self.labRunSt.pack()

		##############END OF FRAME 1 ############################################################

		##############START OF FRAME 2 - Encrypt/Decrypt ############################################################

		self.frame2 = Frame(self.root,borderwidth=0,background='WHITE',)
		self.frame2.pack(fill=BOTH,expand=True,side=BOTTOM)
		########Everything to be in Frame 5################
		self.frame5 = Frame(self.frame2,borderwidth=0,background='GREEN')
		self.encrypt = Button(self.frame5,text="Encrypt",command=lambda: self.onPressEn())
		self.decrypt = Button(self.frame5,text="Decrypt",command=lambda: self.onPressDe())
		self.labInE = Label(self.frame5,text="Enter value for e if encrypting or d if decrypting: ")
		self.inED = Entry(self.frame5)
		self.labInN = Label(self.frame5,text="Enter value for n :")
		self.inN = Entry(self.frame5)
		self.plainOrCyph = Text(self.frame5)
		###################################################
		########Everything being packed in Frame 5#########
		self.frame5.pack(fill=BOTH,expand=True)
		self.labInE.pack()
		self.inED.pack()
		self.labInN.pack()
		self.inN.pack()
		self.encrypt.pack()
		self.decrypt.pack()
		self.plainOrCyph.pack(side=BOTTOM)
		####################################################

	def output(self,e,n,d):
		self.e.insert(0,e)
		self.n.insert(0,n)
		self.d.insert(0,d)
		self.labRunSt.config(text='Stopped')
		return

	def make(self):
		p = self.p.get()
		q = self.q.get()
		p = int(p)
		q = int(q)
		varTup = PubPrivGen(p,q,300,True)
		varlist = list(varTup)
		e = varlist[0]
		n = varlist[1]
		d = varlist[2]
		return(self.output(e,n,d))

	def onPressGen(self):
		self.labRunSt.config(text='Running')
		self.e.delete(0,END)
		self.n.delete(0,END)
		self.d.delete(0,END)
		self.root.update()
		return(self.make())

	def onPressEn(self):
		e = self.inED.get()
		e = int(e)
		n = self.inN.get()
		n = int(n)
		msg = self.plainOrCyph.get("1.0",'end-1c')
		encryptMsg = encrypt(msg,e,n,True)
		self.plainOrCyph.delete(1.0,END)
		self.plainOrCyph.insert(1.0,encryptMsg)
		return

	def onPressDe(self):
		d = self.inED.get()
		d = int(d)
		n = self.inN.get()
		n = int(n)
		cyph = self.plainOrCyph.get("1.0",'end-1c')
		decryptMsg = decrypt(d,n,cyph,True)
		self.plainOrCyph.delete(1.0,END)
		self.plainOrCyph.insert(1.0,decryptMsg)
		return

def main():
    root = Tk()
    gui = Gui(root)
    root.geometry('%dx%d' % (1000,500))
    root.mainloop()

if __name__ == '__main__':
    sys.exit(main())