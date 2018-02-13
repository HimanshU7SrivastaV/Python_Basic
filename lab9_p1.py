from Tkinter import *
root=Tk()
v=IntVar
Label(root,text='select your gender :').pack()
def gen():
    Label(root,text='gender is male ').pack()

def genn():
    Label(root,text='gender is female ').pack()
Radiobutton(root,text='Male',variable=v,value=1,command=gen).pack()
Radiobutton(root,text='Female',variable=v,value=2,command=genn).pack()
root.mainloop()

