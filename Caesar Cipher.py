# @Author: Mohamed Radwan
# @Date: 2018-01-17
# Rotates a list of characters based on the inputed rotate number
# to add an easy way for encryption

import collections
import string
from tkinter import *


def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    popup.mainloop()


def encryption(rotate_string, number_to_rotate_by):
    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)

    upper.rotate(number_to_rotate_by)
    lower.rotate(number_to_rotate_by)

    upper = ''.join(list(upper))
    lower = ''.join(list(lower))

    msg = rotate_string.translate(str.maketrans(string.ascii_uppercase, upper)).translate(
        str.maketrans(string.ascii_lowercase, lower))
    return(msg)


def encrypt():
    encrypted = encryption(e1.get(), int(e2.get()))
    print("Your encryption is: " + encrypted)


def decrypt():
    decrypted = encryption(e1.get(), -int(e2.get()))
    popupmsg("Your decryption is: " + decrypted)

master = Tk()
Label(master, text="Message").grid(row=0)
Label(master, text="Key").grid(row=1)

e1 = Entry(master)
e2 = Entry(master, show="*")

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=5, column=0, sticky=W, pady=4)
Button(master, text='Encrypt', command=encrypt).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Decrypt', command=decrypt).grid(row=4, column=0, sticky=W, pady=4)

mainloop()

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
