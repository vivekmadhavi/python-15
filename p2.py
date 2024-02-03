from tkinter import *
from tkinter.messagebox import *


root=Tk()
root.title("what is next ??")
root.geometry("900x700+100+200")
f=("Arial",40,"bold")



labTitle=Label(root,text="what next app??",font=f)
labTitle.place(x=300,y=20)

labName=Label(root,text="Enter name",font=f)
entName=Entry(root,font=f)
labTitle.place(x=20,y=100)
entName.place(x=350,y=100)


c=IntVar()  #default all are select to prevent them
c.set(1) #select default 1

labChoice=Label(root,text="Select one ",font=f)
entJob=Radiobutton(root,font=f,text="job",variable=c,value=1)
entMs=Radiobutton(root,font=f,text="Ms",variable=c,value=2)
entMba=Radiobutton(root,font=f,text="Mba",variable=c,value=3)
labChoice.place(x=20,y=200)
entJob.place(x=350,y=200)
entMs.place(x=350,y=250)
entMba.place(x=350,y=300)

def save():
	con=None
	try:
		con = connect("wn.db")
		cursor=con.cursor()
		sql="insert into student values('%s','%s')"
		name= entName.get()
		if c.get() == 1:
			choice ="Job"
		elif c.get() == 2:
			choice = "Ms"
		else:
			choice ="Mba"
		cursor.execute(sql %(name,choice))
		con.commit()
		showinfo("success","thanku")
		entName.delete(0,END)
		c.set(1)
		entName.focus()
	except Exception as e:
		con.rollback()
		showerror("issue",str(e))
	finally:
		if con is not None:
			con.close()


btnSubmit = Button(root, text="submit",font=f,command=save)
btnSubmit.place(x=350,y=400)


root.mainloop() 
