from tkinter import *



def plus():
	global first
	global math
	math = "addition"
	first = en.get()
	clear()

def minus():
	global first
	global math
	math = "minus"
	first = en.get()
	clear()
	return

def multiply():
	global first
	global math
	math = "multiphy"
	first = en.get()
	clear()
	return

def division():
	global first
	global math
	math = "division"
	first = en.get()
	clear()

def button_click(number):
	en.insert(END, number)

def clear():
	en.delete(0,END)

def equal():

	if math == "push":
		eq = int(first) + int(en.get())

	if math == "minus":
		eq = int(first) - int(en.get())

	if math == "multiply":
		eq = int(first) * int(en.get())

	if math == "division":
		eq = int(first) / int(en.get())

	clear()

	en.insert(0,eq)


root = Tk()
root.title("Little Calculator")
# Creating a label widget
myLabel = Label(root, text="Hello World")
first = 0
math = ""
en = Entry(root, width=60, borderwidth =5, justify=RIGHT)
en.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

button_1 = Button(root, text="1", padx=40, pady=20, command= lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command= lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command= lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command= lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command= lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command= lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command= lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command= lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command= lambda: button_click(9))
button_0 = Button(root, text="0", padx=137, pady=20, command= lambda: button_click(0))
button_eq = Button(root, text="=", padx=40, pady=20, command= equal)
button_clear = Button(root, text="C", padx=40, pady=20, command=clear)

button_plus = Button(root, text="+", padx=40, pady=20, command=plus)
button_minus = Button(root, text="-", padx=40, pady=20, command=minus)
button_multi = Button(root, text="x", padx=40, pady=20, command=multiply)
button_divide = Button(root, text="/", padx=40, pady=20, command=division)

button_1.grid(row=4, column =1 )
button_2.grid(row=4, column =2 )
button_3.grid(row=4, column =3 )
button_divide.grid(row=4, column= 4)

button_4.grid(row=3, column =1 )
button_5.grid(row=3, column =2 )
button_6.grid(row=3, column =3 )
button_multi.grid(row=3, column= 4)

button_7.grid(row=2, column =1 )
button_8.grid(row=2, column =2 )
button_9.grid(row=2, column =3 )
button_minus.grid(row=2, column= 4)

button_plus.grid(row=1, column= 4)
button_clear.grid(row=1, column =3)


button_0.grid(row=5, column =1, columnspan=3)
button_eq.grid(row=5, column = 4)

root.mainloop()