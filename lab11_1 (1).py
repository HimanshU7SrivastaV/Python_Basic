from Tkinter import *
from tkMessageBox import *
import sqlite3
con=sqlite3.Connection("Emp")
cur=con.cursor()
cur.execute("create table if not exists emp(id number primary key, fname varchar(20),lname varchar(20))")
root=Tk()
x=IntVar()
root.title("Employee Registrartion")
Label(root,text="Employee Record Keeping System:",font="Aerial 15 bold italic",bg='red').grid(row=0,column=0)
Label(root,text="Enter Emp Code:").grid(row=1,column=0,sticky='w')
e=Entry()
e.grid(row=1,column=1)
Label(root,text="Enter First Name:").grid(row=2,column=0,sticky='w')
f=Entry()
f.grid(row=2,column=1)
Label(root,text="Enter Last Name:").grid(row=3,column=0,sticky='w')
l=Entry()
l.grid(row=3,column=1)
Label(root,text="Enter Id to fetch record:").grid(row=4,column=0,sticky='w')
i=Entry()
i.grid(row=4,column=1)
def insert():
    a=(int(e.get()),f.get(),l.get())
    cur.execute("insert into emp values(?,?,?)",a)
    con.commit()
    showinfo('Insert','Insertion Complete')
    cur.execute("select * from emp")
    a=cur.fetchall()
    print a
def show():
    q=int(i.get())
    cur.execute("select * from emp where id=(?)",(q,))
    a=cur.fetchall()
    showinfo('Show',a)
    print a
def showall():
    cur.execute("select * from emp")
    a=cur.fetchall()
    showinfo('Show all',a)
    print a
Button(root,text="Insert",command=insert).grid(row=5,column=0)
Button(root,text="Show",command=show).grid(row=5,column=1,sticky='w')
Button(root,text="Showall",command=showall).grid(row=5,column=2)
root.mainloop()
