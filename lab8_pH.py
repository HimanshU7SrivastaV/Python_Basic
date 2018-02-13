from Tkinter import *
root=Tk()
root.title('facebook')
Label(root,text='enter your name : ').pack()
e=Entry()
e.pack()
Label(root,text='enter your password : ').pack()
p=Entry()
p.pack()
def info():
    Label(root,text='you are successfully login').pack()
def out():
    Label(root,text='are you sure want to cancel').pack()
    Button(root,text='yes',command=fun).pack(),
    Button(root,text='No',command=funn).pack()
    def fun():
        Label(root,text='you are out of this page ').pack()
    def funn():
        Label(root,text='thankyou').pack()
Button(root,text='Login',command=info).pack(),
Button(root,text='Cancel',command=out).pack()
root.mainloop()
