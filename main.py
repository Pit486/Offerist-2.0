import os
from tkinter import *

def bt1(event):
    tk.destroy()
    os.system("python main2.py")
    
def bt2(event):
    print('2')
    
def bt3(event):
    tk.destroy()
    
tk = Tk()
#tk.iconbitmap('i21.ico')
tk.title("Offerist v 2.0")
tk.geometry("305x100")
tk.configure(background="grey")

btn1 = Button(text = 'NEW', width=4, height=1, bg="grey", fg="yellow", font=('Arial Black' ,'18'))
btn1.bind('<Button-1>', bt1)
btn1.place(x=10,y=10)

btn2 = Button(text = 'OPEN', width=4, height=1, bg="grey", fg="yellow", font=('Arial Black' ,'18'))
btn2.bind('<Button-1>', bt2)
btn2.place(x=110,y=10)

btn3 = Button(text = 'EXIT', width=4, height=1, bg="grey", fg="yellow", font=('Arial Black' ,'18'))
btn3.bind('<Button-1>', bt3)
btn3.place(x=210,y=10)

tk.mainloop()
