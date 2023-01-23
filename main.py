import tkinter
from tkinter import *

root=Tk()
root.title("calculette")
root.geometry("600x600+100+200")
root.resizable(False,False)


input_string = ""
def nombre(nombre):
    global input_string
    input_string += str(nombre)
    echo.config(text=input_string)

def point(point):
    global input_string
    input_string += point
    echo.config(text=input_string)

def dele():
    global input_string
    input_string = ""
    echo.config(text=input_string)

def addition():
    global input_string
    input_string += "+"
    echo.config(text=input_string)

def soustraction():
    global input_string
    input_string += "-"
    echo.config(text=input_string)

def multi():
    global input_string
    input_string += "*"
    echo.config(text=input_string)

def division():
    global input_string
    input_string += "/"
    echo.config(text=input_string)

def carre():
    global input_string
    input_string += "** 0.5"
    echo.config(text=input_string)

def factorial():
    global input_string
    input_string += "!"
    echo.config(text=input_string)

def calculer():
    global input_string
    result = eval(input_string)
    input_string = str(result)
    echo.config(text=input_string)


echo= Label(root, text="",width=24, height=2, font=('arial', 30,))#la ou les calcule et les resultats font s'afficher
echo.grid(row=0, column=0)


Button(root, text="del", width=5, height=1, font=('arial', 20, 'bold'), command=dele).place(x=430, y=120)
Button(root, text="1", width=5, height=1, font=('arial', 20, 'bold'), command=lambda: nombre(1)).place(x=10, y=200)
Button(root, text="2", width=5, height=1, font=('arial', 20, 'bold'), command=lambda: nombre(2)).place(x=150, y=200)
Button(root, text="3", width=5, height=1, font=('arial', 20, 'bold'), command=lambda: nombre(3)).place(x=290, y=200)
Button(root, text="4", width=5, height=1, font=('arial', 20, 'bold'), command=lambda: nombre(4)).place(x=10, y=280)
Button(root, text="5", width=5, height=1, font=('arial', 20, 'bold'), command=lambda: nombre(5)).place(x=150, y=280)
Button(root, text="6", width=5, height=1, font=('arial', 20, 'bold'), command=lambda: nombre(6)).place(x=290, y=280)
Button(root, text="7", width=5, height=1, font=('arial', 20, 'bold'), command=lambda: nombre(7)).place(x=10, y=360)
Button(root, text="8", width=5, height=1, font=('arial', 20, 'bold'), command=lambda: nombre(8)).place(x=150, y=360)
Button(root, text="9", width=5, height=1, font=('arial', 20, 'bold'), command=lambda: nombre(9)).place(x=290, y=360)
Button(root, text="0", width=5, height=1, font=('arial', 20, 'bold'), command=lambda: nombre(0)).place(x=10, y=440)
Button(root, text=".", width=5, height=1, font=('arial', 20, 'bold'), command=lambda: point(".")).place(x=150, y=440)
Button(root, text="=", width=5, height=1, font=('arial', 20, 'bold'), command=calculer).place(x=290, y=440)
Button(root, text="+", width=5, height=1, font=('arial', 20, 'bold'), command=addition).place(x=430, y=200)
Button(root, text="-", width=5, height=1, font=('arial', 20, 'bold'), command=soustraction).place(x=430, y=280)
Button(root, text="*", width=5, height=1, font=('arial', 20, 'bold'), command=multi).place(x=430, y=360)
Button(root, text="/", width=5, height=1, font=('arial', 20, 'bold'), command=division).place(x=430, y=440)





root.mainloop()