from Tkinter import *
root=Tk()
v1=IntVar()
v2=IntVar()
v3=IntVar()
v4=IntVar()
root.title('my favourite colour')
Label(root,text='selecr your favourite colour ').pack()
Checkbutton(root,text='Red',variable=v1,onvalue=10).pack()
Checkbutton(root,text='Green',variable=v2,onvalue=20).pack()
Checkbutton(root,text='Yellow',variable=v3,onvalue=30).pack()
Checkbutton(root,text='Purple',variable=v4,onvalue=40).pack()
def fun():
    if v1.get()==10:
        Label(root,text='your favourite colour is RED').pack()
    elif v2.get()==20:
        Label(root,text='your favourite colour is GREEN').pack()
    elif v3.get()==30:
        Label(root,text='your favourite colour is YELLOW').pack()
    elif v4.get()==40:
        Label(root,text='your favourite colour is PURPLE').pack()
Button(root,text='Go',command=fun).pack()
root.mainloop()
