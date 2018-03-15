from os import listdir
from os.path import isfile, join
from os import walk
import os
import sys
#from pymongo import MongoClient
import magic

class Folder_Info:
	def __init__(self, folder_path):
		self.path=folder_path
		self.num_of_files=0
		self.file_list=[]

	def get_file_names(self):
		path=self.path
		for(dirpath,dirnames,filenames) in walk(self.path):
			for file in filenames:
				p=os.path.join(dirpath,file)
				p=os.path.abspath(p)
				self.file_list.append(p.replace(" ","\ "))
		self.num_of_files=len(self.file_list)
	'''
	def get_metadata(self):
		for file in self.file_list:
			print "************ ",file," **************"
			if self.m.file(file) != None:
				if self.m.file(file).split(";")[0]=="text/plain":
					print "Plain Text"
				else:
					os.system("hachoir-metadata "+file)
	'''

	def get_file_list(self):
		return self.file_list

	
		
#if len(sys.argv)==2:
#	folder_path=sys.argv[1]
#else:
#	print "Usage: python Read.py <folder_path>"
#	sys.exit()

'''
if __name__ == "__main__":
	a=Folder_Info(folder_path)
	a.get_file_names()
	a.get_metadata()
	a.get_file_type()
'''
