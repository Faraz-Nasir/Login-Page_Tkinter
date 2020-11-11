from tkinter import *
import time
from tkinter import messagebox

def clear():
    name_label_entry.delete(0,END)
    contact_label_entry.delete(0,END)
    email_label_entry.delete(0,END)

def submit():

    if(len(name_label_entry.get())==0 or len(contact_label_entry.get())==0 or len(email_label_entry.size())==0):
        response=messagebox.showwarning("ERROR","Please Fill all The Columns")
        Label(root,text=response).pack()

    name = name_label_entry.get()
    contact = contact_label_entry.get()
    email = email_label_entry.get()
    clear()



root=Tk()
root.title("MyForm Desktop App")
root.resizable(0,0)
root.geometry('500x700')

seconds=time.localtime()
date=f"{seconds[2]}/{seconds[1]}/{seconds[0]}"
time=f"{seconds[3]}:{seconds[4]}:{seconds[5]}"

frame1=PanedWindow(bd=4,relief="raised",bg="red",height=400)
frame1.pack(fill=BOTH,expand=1)

frame1_sub1=PanedWindow(bd=4,relief="raised",bg="blue",width=200)
frame1_sub2=PanedWindow(bd=4,relief="raised",bg="white",orient=VERTICAL)
frame1.add(frame1_sub1)
frame1.add(frame1_sub2)

start_label=Label(frame1_sub2,text="ENTRY FORM",font=("Helvetica",14))
start_label.grid(row=0,column=1,padx=(9,0),sticky=W,pady=(6,20))


name_label=Label(frame1_sub2,text="Your Name",font=("Helvetica",10))
name_label.grid(row=1,column=0,pady=(20,0),sticky=W)
name_label_entry=Entry(frame1_sub2)
name_label_entry.grid(row=1,column=1,pady=(20,0))

contact_label=Label(frame1_sub2,text="Contact",font=("Helvetica",10))
contact_label.grid(row=2,column=0,pady=(20,0),sticky=W)
contact_label_entry=Entry(frame1_sub2)
contact_label_entry.grid(row=2,column=1,pady=(20,0))

email_label=Label(frame1_sub2,text="Email Address",font=("Helvetica",10))
email_label.grid(row=3,column=0,pady=(20,0),sticky=W)
email_label_entry=Entry(frame1_sub2)
email_label_entry.grid(row=3,column=1,pady=(20,0))

btn_submit=Button(frame1_sub2,text="SUBMIT",bg="green",command=submit)
btn_submit.grid(row=4,column=0,pady=(20,0),padx=(60,0))

btn_clear=Button(frame1_sub2,text="CLEAR",bg="red",command=clear)
btn_clear.grid(row=4,column=1,pady=(20,0))

frame2=PanedWindow(bd=4,relief="raised",bg="green")
frame2.pack(fill=BOTH,expand=1)

time_label=Label(frame2,text=f"TIME:- {time}",font=("Helvetica",20))
time_label.grid(row=0,column=0,sticky=W)

date_label=Label(frame2,text=f"DATE:- {date}",font=("Helvetica",20))
date_label.grid(row=1,column=0,sticky=W)


root.mainloop()
