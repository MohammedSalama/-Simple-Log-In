#######By Muhammed Salama ########
from Tkinter import *

window=Tk()

l1=Label(window,text='User name:')
l2=Label(window,text='Password:')

t1=Entry(window,textvariable=StringVar())
t2=Entry(window,textvariable=StringVar())

b1=Button(window,text='Log.in')

l1.pack()
t1.pack()
l2.pack()
t2.pack()
b1.pack()

window.mainloop()


