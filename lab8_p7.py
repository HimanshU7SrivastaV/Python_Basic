from Tkinter import *
root=Tk()
root.title('HAPPY BIRTHDAY')
Label(root,text='enter your firstname : ').pack()
e=Entry()
e.pack()
Label(root,text='enter your last name : ').pack()
p=Entry()
p.pack()
def info():
    Label(root,text='hey ! '+e.get()+'HAPPY BIRTHDAY ').pack()
Button(root,text='Go',command=info).pack()
root.mainloop()
