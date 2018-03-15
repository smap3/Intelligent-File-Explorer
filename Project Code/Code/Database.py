#Database file that supports all database operations, written so that the file can simply be imported and used as a wrapper for database operations.
from pymongo import MongoClient

class Database:
	def __init__(self,database_name):
		self.client=MongoClient("localhost:27017")
		self.db=self.client[database_name]
		self.collection=None

	def set_collection(self, collection_name):
		self.collection=self.db[collection_name]

	def add_entry(self,key,value):
		self.collection.insert({key:value})

	def search_Files(self,search_key):
		#return self.collection.find({search_key,"/home/nsk/Test.mp3"})
		return self.collection.find({},{search_key:1,'_id':0})

	def close(self):
		self.client.close()
'''
if __name__=='__main__':
	a=Database("FirstDatabase")
	a.add_collection("Countries")
	a.add_entry("Name","India")
	b=db.countries.find({"name"://})
	for doc in b:
		at1=doc["name"]
		print at1
	print a.get_country()


	> var a=db.countries.find({},{_id:0})
> a[0]['name']
India
> var a=db.countries.find({},{name:1,_id:0})
> a[0]['name']
India
> 

'''