# @Author: Mohamed Radwan
# @Date: 2018-01-17
# Rotates a list of characters based on the inputed rotate number
# to add an easy way for encryption

import collections
import string
import ctypes
from tkinter import *

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

def encryption(rotate_string, number_to_rotate_by):
    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)

    upper.rotate(number_to_rotate_by)
    lower.rotate(number_to_rotate_by)

    upper = ''.join(list(upper))
    lower = ''.join(list(lower))

    msg = rotate_string.translate(str.maketrans(string.ascii_uppercase, upper)).translate(str.maketrans(string.ascii_lowercase, lower))
    popupmsg (msg)


root = Tk()
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)


label1 = Label(topFrame, text = "Welcome to my encryption and decryption software")
label1.pack()

labelMsg = Label(topFrame, text="Message")
labelMsg.pack(side = LEFT)
msg = Entry(topFrame)
msg.pack(side = LEFT)

labelKey = Label(topFrame, text="Key")
labelKey.pack(side = LEFT)
key = Entry(topFrame,show = "*")
key.pack(side = LEFT)

btn1 = Button(bottomFrame,text="Encrypt", command = lambda: encryption(msg,key))
btn2 = Button(bottomFrame,text="Decrypt", command = lambda: encryption(msg,-key))
btn1.pack(side=LEFT)
btn2.pack(side=RIGHT)
root.mainloop()


# stop = True
# print("Welcome to my encryption and decryption software")
# while (stop):
#
#         service = input("1 for encryption\n2 for decryption\n")
#         string = raw_input("Please input your text\n")
#         key = input("Please input the key\n")
#         if service == 1:
#             print("The encrypted text is: ", caesar(string, key))
#         elif service == 2:
#             print("The decrypted text is: ", caesar(string, - key))
#         else:
#             print("Thats an invalid input please try again")
