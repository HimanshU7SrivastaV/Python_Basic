from Tkinter import *
from tkMessageBox import *
import sqlite3
con=sqlite3.Connection("Stu")
cur=con.cursor()
cur.execute("create table if not exists stu(id number primary key, fname varchar(20),lname varchar(20),dob number,father_name varchar(20),course varchar(20),dept varchar(20),registration varchar(7),address varchar(56),mob number,cgpa number)")
root=Tk()
x=IntVar()
root.title("Student Registrartion")
Label(root,text="Student Record Keeping System:",font="Aerial 15 bold italic",bg='red').grid(row=0,column=0)
Label(root,text="Enter Enrolment no:").grid(row=1,column=0,sticky='w')
e=Entry()
e.grid(row=1,column=1)
Label(root,text="Enter First Name:").grid(row=2,column=0,sticky='w')
f=Entry()
f.grid(row=2,column=1)
Label(root,text="Enter Last Name:").grid(row=3,column=0,sticky='w')
l=Entry()
l.grid(row=3,column=1)
Label(root,text="Enter Date of birth:").grid(row=4,column=0,sticky='w')
d=Entry()
d.grid(row=4,column=1)
Label(root,text="Enter Father`s Name:").grid(row=5,column=0,sticky='w')
fa=Entry()
fa.grid(row=5,column=1)
Label(root,text="Enter Course:").grid(row=6,column=0,sticky='w')
c=Entry()
c.grid(row=6,column=1)
Label(root,text="Enter Department:").grid(row=7,column=0,sticky='w')
de=Entry()
de.grid(row=7,column=1)
Label(root,text="Enter registration date:").grid(row=8,column=0,sticky='w')
re=Entry()
re.grid(row=8,column=1)
Label(root,text="Enter Your Address:").grid(row=9,column=0,sticky='w')
add=Entry()
add.grid(row=9,column=1)
Label(root,text="Enter Your Mobile No.:").grid(row=10,column=0,sticky='w')
mo=Entry()
mo.grid(row=10,column=1)
Label(root,text="Enter Your Cgpa:").grid(row=11,column=0,sticky='w')
c=Entry()
c.grid(row=11,column=1)
Label(root,text="Enter Er No. to fetch record:").grid(row=12,column=0,sticky='w')
i=Entry()
i.grid(row=12,column=1)
def insert():
    b=(int(e.get()),f.get(),l.get(),d.get(),fa.get(),c.get(),de.get(),re.get(),add.get(),mo.get(),c.get())
    cur.execute("insert into stu values(?,?,?,?,?,?,?,?,?,?,?)",b)
    con.commit()
    showinfo('Insert','Insertion Complete')
    cur.execute("select * from stu")
    b=cur.fetchall()
    print b
def show():
    q=int(i.get())
    cur.execute("select * from stu where id=(?)",(q,))
    a=cur.fetchall()
    showinfo('Show',a)
    print a
def showall():
    cur.execute("select * from stu")
    a=cur.fetchall()
    showinfo('Show all',a)
    print a
Button(root,text="Insert",command=insert).grid(row=13,column=0)
Button(root,text="Show",command=show).grid(row=13,column=1,sticky='w')
Button(root,text="Showall",command=showall).grid(row=13,column=2)
root.mainloop()