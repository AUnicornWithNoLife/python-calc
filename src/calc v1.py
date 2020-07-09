import tkinter as tk
from math import *

m = tk.Tk()

no = ""
nos = ""

def update():
    out.delete(1.0, tk.END)
    out.insert(tk.END, no)

def one():
    global no, nos

    nom = str(no + "1")
    no = nom
    nos = nom

    update()

def two():
    global no, nos

    nom = str(no + "2")
    no = nom
    nos = nom

    update()

def three():
    global no, nos

    nom = str(no + "3")
    no = nom
    nos = nom

    update()

def four():
    global no, nos

    nom = str(no + "4")
    no = nom
    nos = nom

    update()

def five():
    global no, nos

    nom = str(no + "5")
    no = nom
    nos = nom

    update()

def six():
    global no, nos

    nom = str(no + "6")
    no = nom
    nos = nom

    update()

def seven():
    global no, nos

    nom = str(no + "7")
    no = nom
    nos = nom

    update()

def eight():
    global no, nos

    nom = str(no + "8")
    no = nom
    nos = nom

    update()

def nine():
    global no, nos

    nom = str(no + "9")
    no = nom
    nos = nom

    update()

def zero():
    global no, nos

    nom = str(no + "0")
    no = nom
    nos = nom

    update()

def eq():
    global no, nos

    print(no)

    calc(str(eval(no)))

def calc(n):
    global no, nos

    print(n)

    no = n
    nos = no
    update()

def plus():
    global no, nos

    nom = str(no + "+")
    no = nom
    nos = nom

    update()

def minus():
    global no, nos

    nom = str(no + "-")
    no = nom
    nos = nom

    update()

def times():
    global no, nos

    nom = str(no + "*")
    no = nom
    nos = nom

    update()

def divide():
    global no, nos

    nom = str(no + "/")
    no = nom
    nos = nom

    update()

def back():
    global no, nos

    nom = no[:-1]
    no = nom
    nos = nom

    calc(nom)

def clear():
    no = ''
    
    calc('')

def dec():
    global no, nos

    nom = str(no + ".")
    no = nom
    nos = nom

    update()

def sqrt():
    global no, nos

    nom = str(no + "sqrt")
    no = nom
    nos = nom

    update()

def b1():
    global no, nos

    nom = str(no + "(")
    no = nom
    nos = nom

    update()

def b2():
    global no, nos

    nom = str(no + ")")
    no = nom
    nos = nom

    update()

m.title("Calculator")
m.wm_iconbitmap('favicon.ico')

top = tk.Frame(m)
L0 = tk.Frame(m)
L1 = tk.Frame(m)
L2 = tk.Frame(m)
L3 = tk.Frame(m)
L4 = tk.Frame(m)

top.pack()
L0.pack()
L1.pack()
L2.pack()
L3.pack()
L4.pack()

out = tk.Text(top, height=2, width=32) 
out.pack()

one = tk.Button(L1, text="1", command=one, width=8, height=4)
one.pack(side=tk.LEFT)
two = tk.Button(L1, text="2", command=two, width=8, height=4)
two.pack(side=tk.LEFT)
three = tk.Button(L1, text="3", command=three, width=8, height=4)
three.pack(side=tk.LEFT)
four = tk.Button(L2, text="4", command=four, width=8, height=4)
four.pack(side=tk.LEFT)
five = tk.Button(L2, text="5", command=five, width=8, height=4)
five.pack(side=tk.LEFT)
six = tk.Button(L2, text="6", command=six, width=8, height=4)
six.pack(side=tk.LEFT)
seven = tk.Button(L3, text="7", command=seven, width=8, height=4)
seven.pack(side=tk.LEFT)
eight = tk.Button(L3, text="8", command=eight, width=8, height=4)
eight.pack(side=tk.LEFT)
nine = tk.Button(L3, text="9", command=nine, width=8, height=4)
nine.pack(side=tk.LEFT)
zero = tk.Button(L4, text="0", command=zero, width=8, height=4)
zero.pack(side=tk.LEFT)


minus = tk.Button(L1, text="-", command=minus, width=8, height=4)
minus.pack(side=tk.LEFT)
times = tk.Button(L2, text="*", command=times, width=8, height=4)
times.pack(side=tk.LEFT)
divide = tk.Button(L3, text="/", command=divide, width=8, height=4)
divide.pack(side=tk.LEFT)
dec = tk.Button(L4, text=".", command=dec, width=8, height=4)
dec.pack(side=tk.LEFT)
sqrt = tk.Button(L0, text="SQRT", command=sqrt, width=8, height=4)
sqrt.pack(side=tk.LEFT)
equal = tk.Button(L4, text="=", command=eq, width=17, height=4)
equal.pack(side=tk.LEFT)

clear = tk.Button(L0, text="ac", command=clear, width=8, height=4)
clear.pack(side=tk.LEFT)

back = tk.Button(L0, text="c", command=back, width=8, height=4)
back.pack(side=tk.LEFT)

plus = tk.Button(L0, text="+", command=plus, width=8, height=4)
plus.pack(side=tk.LEFT)

b1 = tk.Button(L0, text="(", command=b1, width=8, height=4)
b1.pack(side=tk.LEFT)
b2 = tk.Button(L1, text=")", command=b2, width=8, height=4)
b2.pack(side=tk.LEFT)


m.mainloop()
