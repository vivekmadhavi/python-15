#wapp to create studnt record

from pymongo import *
con = None
try:
	con=MongoClient("localhost",27017)
	db = con ["kc_23dec23"]
	coll = db["student"]

	rno = int(input("enter no "))
	name= input("enter name ")
	marks = int(input("enter marks "))

	info ={"_id":rno,"name":name,"marks":marks}
	coll.insert_one(info)
	print("record created")

except Exception as e:
	print("issue",e)
finally:
	if con is not None:
		con.close()