from Tkinter import *
root=Tk()
root.title('CALCULATOR')
Label(root,text='we are going to perform the calculations ......')
Label(root,text='enter the number : ').pack()
e1=Entry()
e1.pack()
Label(root,text='enter the number : ').pack()
e2=Entry()
e2.pack()
m=e1.get()
n=e2.get()
def out():
    Label(root,text=m+n).pack()
def info():
    Label(root,text=m-n).pack()
def fun():
    Label(root,text=m*n).pack()
def funn():
    Label(root,text=m/n).pack()
Button(root,text='Sum',command=out).pack()
Button(root,text='Difference',command=info).pack()
Button(root,text='Multiply',command=fun).pack()
Button(root,text='Division',command=funn).pack()
root.mainloop()
