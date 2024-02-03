from  sqlite3 import *

name=input("enter the name")

ch=int(input("press 1 job, press 2 ms, press 3 mba"))
if ch ==1:
	choice = "job"
elif ch == 2:
	choice = "MS"
else:
	choice ="MBA"
con=None
try:
	con = connect("wn.db")
	cursor=con.cursor()
	sql="insert into student values('%s','%s')"
	cursor.execute(sql %(name,choice))
	con.commit()
	print("thanku")
except Exception as e:
	con.rollback()
	print("issue",e)
finally:
	if con is not None:
		con.close() 