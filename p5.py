#wapp to create studnt record

from pymongo import *
con = None
try:
	con=MongoClient("localhost",27017)
	db = con ["kc_23dec23"]
	coll = db["student"]

	data = coll.find()
	for d in data:
		print(d)
except Exception as e:
	print("issue",e)
finally:
	if con is not None:
		con.close()