from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *

#Available Module imports
import os, sys
import magic

#UI Imports
import Design
import ProgressDesign
import Display
import Association

#Import for WebUI
from PyQt4.QtWebKit import *

#Custom Module imports
from Read import Folder_Info

#global variables
directory=""
basic_flag=0

#subprocess
import subprocess

#hachoir imports:

from hachoir_core.cmd_line import unicodeFilename
from hachoir_parser import createParser
from hachoir_core.tools import makePrintable
from hachoir_metadata import extractMetadata
from hachoir_core.i18n import getTerminalCharset
from sys import argv, stderr, exit

#Database import
from Database import Database

#for copying file
import shutil

class Association(QtGui.QMainWindow,Association.Ui_MainWindow):
	def __init__(self, parent=None):
		super(self.__class__,self).__init__(parent)
		self.setupUi(self)
		self.centerOnScreen()
		self.display()

	def centerOnScreen(self):
		resolution = QtGui.QDesktopWidget().screenGeometry()
		self.move((resolution.width() / 2) - (self.frameSize().width() / 2),(resolution.height() / 2) - (self.frameSize().height() / 2))

	def display(self):
		file1=open("/home/nsk/Desktop/Start/Begin1/Output/Associated_Topics/assoc1.txt","r+")
		file1_data=file1.readlines()
		file2=open("/home/nsk/Desktop/Start/Begin1/Output/Associated_Topics/assoc2.txt","r+")
		file2_data=file2.readlines()
		self.TW_Assoc.setRowCount(len(file1_data))
		for i in range(0,len(file1_data)):
			self.TW_Assoc.setItem(i,0,QTableWidgetItem(file1_data[i].strip('\n')))
			print file1_data[i].strip('\n')
		for i in range(0,len(file1_data)):
			self.TW_Assoc.setItem(i,1,QTableWidgetItem(file2_data[i].strip('\n')))

		file1.close()
		file2.close()

class Display(QtGui.QMainWindow,Display.Ui_MainWindow):
	def __init__(self, parent=None):
		super(self.__class__,self).__init__(parent)
		self.setupUi(self)
		self.centerOnScreen()
		#self.test()
		self.PB_td.clicked.connect(self.display_td)
		self.PB_cp.clicked.connect(self.display_cp)
		self.PB_as.clicked.connect(self.display_as)

	def display_as(self):
		self.form4=Association(self)
		self.form4.show()

	def display_td(self):
		os.system("xdg-open /home/nsk/Desktop/Start/Begin1/vis10/index.html")

	def display_cp(self):
		os.system("xdg-open /home/nsk/Desktop/Start/Begin1/Rplots.pdf")
	
	def test(self):
		self.TW_Table.setRowCount(5)
		#temp=QTableWidgetItem(QString("HEADER 1 \n Header_nextline"))
		#temp2=QTableWidgetItem('Hellodasfadsfadfadfa \nHello\nHello\nHello')
		#self.TW_Table.setItem(1,1,temp)
		#self.TW_Table.setItem(4,1,temp2)
		fp1=open("/home/nsk/Desktop/Start/Begin1/Output/Terms/1.txt","r+")
		fp2=open("/home/nsk/Desktop/Start/Begin1/Output/Terms/2.txt","r+")
		fp3=open("/home/nsk/Desktop/Start/Begin1/Output/Terms/3.txt","r+")
		fp4=open("/home/nsk/Desktop/Start/Begin1/Output/Terms/4.txt","r+")
		fp5=open("/home/nsk/Desktop/Start/Begin1/Output/Terms/5.txt","r+")

		fp1_content=fp1.readlines()
		str=""
		for i in range(0,len(fp1_content)):
			str=str+fp1_content[i]
		self.TW_Table.setItem(0,1,QTableWidgetItem(str))

		fp1_content=fp2.readlines()
		str=""
		for i in range(0,len(fp1_content)):
			str=str+fp1_content[i]
		self.TW_Table.setItem(1,1,QTableWidgetItem(str))

		fp1_content=fp3.readlines()
		str=""
		for i in range(0,len(fp1_content)):
			str=str+fp1_content[i]
		self.TW_Table.setItem(2,1,QTableWidgetItem(str))

		fp1_content=fp4.readlines()
		str=""
		for i in range(0,len(fp1_content)):
			str=str+fp1_content[i]
		self.TW_Table.setItem(3,1,QTableWidgetItem(str))

		fp1_content=fp5.readlines()
		str=""
		for i in range(0,len(fp1_content)):
			str=str+fp1_content[i]
		self.TW_Table.setItem(4,1,QTableWidgetItem(str))

		fp1.close()
		fp2.close()
		fp3.close()
		fp4.close()
		fp5.close()

		self.TW_Table.setItem(0,0,QTableWidgetItem("1"))
		self.TW_Table.setItem(1,0,QTableWidgetItem("2"))
		self.TW_Table.setItem(2,0,QTableWidgetItem("3"))
		self.TW_Table.setItem(3,0,QTableWidgetItem("4"))

		fp1=open("/home/nsk/Desktop/Start/Begin1/Output/Clusters/1.txt","r+")
		fp2=open("/home/nsk/Desktop/Start/Begin1/Output/Clusters/2.txt","r+")
		fp3=open("/home/nsk/Desktop/Start/Begin1/Output/Clusters/3.txt","r+")
		fp4=open("/home/nsk/Desktop/Start/Begin1/Output/Clusters/4.txt","r+")
		fp5=open("/home/nsk/Desktop/Start/Begin1/Output/Clusters/5.txt","r+")

		fp11=open("/home/nsk/Desktop/Start/Begin1/Output/Clusters_Final/1.txt","wb+")
		fp22=open("/home/nsk/Desktop/Start/Begin1/Output/Clusters_Final/2.txt","wb+")
		fp33=open("/home/nsk/Desktop/Start/Begin1/Output/Clusters_Final/3.txt","wb+")
		fp44=open("/home/nsk/Desktop/Start/Begin1/Output/Clusters_Final/4.txt","wb+")
		fp55=open("/home/nsk/Desktop/Start/Begin1/Output/Clusters_Final/5.txt","wb+")

		fp1_content=fp1.readlines()
		fp2_content=fp2.readlines()
		fp3_content=fp3.readlines()
		fp4_content=fp4.readlines()
		fp5_content=fp5.readlines()

		
		for i in range(0,len(fp1_content)):
			search_key=fp1_content[i].strip('\n').replace(".",";")
			#print search_key
			a=Database("MuDaM")
			a.set_collection("Files")
			returned_key=a.search_Files(search_key)
			for i in returned_key:
				if i:
					fp11.write(i[search_key].replace(";",".")+"\n")
					print i[search_key].replace(";",".")+"\n"
			a.close()

		for i in range(0,len(fp2_content)):
			search_key=fp2_content[i].strip('\n').replace(".",";")
			#print search_key
			a=Database("MuDaM")
			a.set_collection("Files")
			returned_key=a.search_Files(search_key)
			for i in returned_key:
				if i:
					fp22.write(i[search_key].replace(";",".")+"\n")
					print i[search_key].replace(";",".")+"\n"
			a.close()

		for i in range(0,len(fp3_content)):
			search_key=fp3_content[i].strip('\n').replace(".",";")
			#print search_key
			a=Database("MuDaM")
			a.set_collection("Files")
			returned_key=a.search_Files(search_key)
			for i in returned_key:
				if i:
					fp33.write(i[search_key].replace(";",".")+"\n")
					print i[search_key].replace(";",".")+"\n"
			a.close()

		for i in range(0,len(fp4_content)):
			search_key=fp4_content[i].strip('\n').replace(".",";")
			#print search_key
			a=Database("MuDaM")
			a.set_collection("Files")
			returned_key=a.search_Files(search_key)
			for i in returned_key:
				if i:
					fp44.write(i[search_key].replace(";",".")+"\n")
					print i[search_key].replace(";",".")+"\n"
			a.close()

		for i in range(0,len(fp5_content)):
			search_key=fp5_content[i].strip('\n').replace(".",";")
			#print search_key
			a=Database("MuDaM")
			a.set_collection("Files")
			returned_key=a.search_Files(search_key)
			for i in returned_key:
				if i:
					fp55.write(i[search_key].replace(";",".")+"\n")
					print i[search_key].replace(";",".")+"\n"
			a.close()

		#key_string_1=key_string.replace(".",";")
		#value_string_1=value_string.replace(".",";")
		#a=Database("MuDaM")
		#a.set_collection("Files")
		#a.add_entry(key_string_1,value_string_1)
		#a.close()

		self.TW_Table.resizeColumnsToContents()
		self.TW_Table.resizeRowsToContents()
		self.TW_Table.hide()
		self.TW_Table.show()

		fp1.close()
		fp2.close()
		fp3.close()
		fp4.close()
		fp5.close()

		fp11.close()
		fp22.close()
		fp33.close()
		fp44.close()
		fp55.close()

		fp1=open("/home/nsk/Desktop/Start/Begin1/Output/Clusters_Final/1.txt","r+")
		fp2=open("/home/nsk/Desktop/Start/Begin1/Output/Clusters_Final/2.txt","r+")
		fp3=open("/home/nsk/Desktop/Start/Begin1/Output/Clusters_Final/3.txt","r+")
		fp4=open("/home/nsk/Desktop/Start/Begin1/Output/Clusters_Final/4.txt","r+")
		fp5=open("/home/nsk/Desktop/Start/Begin1/Output/Clusters_Final/5.txt","r+")

		fp1_content=fp1.readlines()
		str=""
		for i in range(0,len(fp1_content)):
			str=str+fp1_content[i]
		self.TW_Table.setItem(0,2,QTableWidgetItem(str))

		fp1_content=fp2.readlines()
		str=""
		for i in range(0,len(fp1_content)):
			str=str+fp1_content[i]
		self.TW_Table.setItem(1,2,QTableWidgetItem(str))

		fp1_content=fp3.readlines()
		str=""
		for i in range(0,len(fp1_content)):
			str=str+fp1_content[i]
		self.TW_Table.setItem(2,2,QTableWidgetItem(str))

		fp1_content=fp4.readlines()
		str=""
		for i in range(0,len(fp1_content)):
			str=str+fp1_content[i]
		self.TW_Table.setItem(3,2,QTableWidgetItem(str))

		fp1_content=fp5.readlines()
		str=""
		for i in range(0,len(fp1_content)):
			str=str+fp1_content[i]
		self.TW_Table.setItem(4,2,QTableWidgetItem(str))


		fp1.close()
		fp2.close()
		fp3.close()
		fp4.close()




	def centerOnScreen(self):
		resolution = QtGui.QDesktopWidget().screenGeometry()
		self.move((resolution.width() / 2) - (self.frameSize().width() / 2),(resolution.height() / 2) - (self.frameSize().height() / 2))


class ProgressClass(QtGui.QMainWindow,ProgressDesign.Ui_ProgressWindow):
	def __init__(self,parent=None):
		super(self.__class__,self).__init__(parent)
		self.setupUi(self)
		self.completed=0
		self.centerOnScreen()

	def update_progress(self,msg,increment):
		self.TB_ProgressLog.append("* "+msg+"...")
		increment=self.completed+increment
		while self.completed<=increment and self.completed<=100:
			self.completed+=0.00001
			self.PB_ProgressBar.setValue(self.completed)

	def update_message(self,msg):
		self.TB_ProgressLog.append("* "+msg+"...")


	def update_value(self,increment):
		increment=self.completed+increment
		while self.completed<=increment and self.completed<=100:
			self.completed+=0.00001
			self.PB_ProgressBar.setValue(self.completed)

	def centerOnScreen(self):
		resolution = QtGui.QDesktopWidget().screenGeometry()
		self.move((resolution.width() / 2) - (self.frameSize().width() / 2),(resolution.height() / 2) - (self.frameSize().height() / 2))



class MainClass(QtGui.QMainWindow,Design.Ui_MainWindow):
	def __init__(self,parent=None):
		super(self.__class__,self).__init__(parent)
		self.setupUi(self)
		self.centerOnScreen()
		self.BTN_SelFolder.clicked.connect(self.browse_folder)
		self.BTN_Process.clicked.connect(self.process_folder)
		self.actionAuthors.triggered.connect(self.show_authors)
		self.form2=ProgressClass(self)
		self.form3=Display(self)
		self.magic=magic.open(magic.MAGIC_MIME)
		self.magic.load()
		#Test

	def centerOnScreen(self):
		resolution = QtGui.QDesktopWidget().screenGeometry()
		self.move((resolution.width() / 2) - (self.frameSize().width() / 2),(resolution.height() / 2) - (self.frameSize().height() / 2))

	def browse_folder(self):
		global directory
		directory=QtGui.QFileDialog.getExistingDirectory(self,"Pick a folder")
		directory=str(directory)
		self.LE_FolderPath.setText(directory)
		self.LE_FolderPath.setEnabled(False)

	def process_folder(self):
		global basic_flag
		if self.RB_BasicClustering.isChecked()==True:
			basic_flag=1
		#elif self.RB_IntClustering.isChecked()==True:
			#basic_flag=2
		elif self.RB_AdvClustering.isChecked()==True:
			basic_flag=2
		#global directory
		#a=Database("MuDaM")
		#a.set_collection("Main")
		#a.add_entry("Directory",directory)
		#print a.get_entry()
		#a.close
		self.hide()
		self.form2.show()
		self.get_listing()

	def show_authors(self):
		msg=QMessageBox()
		msg.setIcon(QMessageBox.Information)
		msg.setWindowTitle("About")
		msg.setText("Developed By:\nPune Institute of Computer Technology, Dhankawadi, Pune")
		msg.setDetailedText("Authors:\n1. Nikhil Kulkarni\n2. Shubham Khirade\n3. Shubham Pathak\n4. Soham Lawar\nUnder the guidance of: Dr. Parag Kulkarni")
		msg.setStandardButtons(QMessageBox.Ok)
		msg.show()
		msg.exec_()

	def get_listing(self):
		global directory
		a=Folder_Info(directory)
		a.get_file_names()
		self.file_list=a.get_file_list()
		self.form2.update_progress("Listing all files",20)
		self.separate_files()

	def separate_files(self):
		self.form2.update_progress("Getting file types",10)
		#Feature Extraction from images
		self.form2.update_message("Extracting features from images. Please wait")
		i=0
		j=0
		k=0
		l=0
		for file in self.file_list:
			#file=file.replace("\ "," ")
			file_type=self.magic.file(file).split(";")[0]
			if 'image' in file_type:
				i=i+1
				#print file+":"+'image'
				self.form2.update_value(1)
				subprocess.call(['python','/home/nsk/Project/caffe/examples/caffe_example.py',file])
			if 'audio' in file_type:
				j=j+1
				#update while processing
				self.form2.update_value(1)
				#self.tb_metadata.append("**** Metadata for: "+file+" ****")
				filename = file
				filename, realname = unicodeFilename(filename), filename
				parser = createParser(filename, realname)
				if not parser:
					print >>stderr, "Unable to parse file"
					continue
	                #exit(1)
				try:
				    metadata = extractMetadata(parser)
				except Exception as err:
				    print "Metadata extraction error: %s" % unicode(err)
				    metadata = None
				if not metadata:
				    print "Unable to extract metadata"
				    continue
	                #exit(1)
				text = metadata.exportPlaintext()
				charset = getTerminalCharset()
	            #create corresponding text file
				value_string=file
				key_string="/home/nsk/Desktop/Start/Begin1/Files/"+value_string.split("/")[-1].split(".")[0]+"."+"txt"
				#write metadata to the file
				fp=open(key_string,"wb+")
				for line in text:
					fp.write(line)
				fp.close()
	            #write the key, value to the database
				key_string_1=key_string.replace(".",";")
				value_string_1=value_string.replace(".",";")
				a=Database("MuDaM")
				a.set_collection("Files")
				a.add_entry(key_string_1,value_string_1)
				a.close()
			if 'text' in file_type:
				k=k+1
				path="/home/nsk/Desktop/Start/Begin1/Files/"
				path2=file.split("/")[-1]
				dest_path=path+path2
				src_path=file
				shutil.copy2(src_path,dest_path)
				key_string=dest_path.replace(".",";")
				value_string=src_path.replace(".",";")
				a=Database("MuDaM")
				a.set_collection("Files")
				a.add_entry(key_string,value_string)
				a.close()
			if 'video' in file_type:
				l=l+1
				command='ffmpeg -ss 3 -i file -vf "select=gt(scene\,0.4)" -frames:v 5 -vsync vfr /home/nsk/Desktop/Start/Begin1/FilesV/out%02d.jpg'
				subprocess.call([command])


		self.form2.update_message("Analysed "+str(i)+" images")
		self.form2.update_message("Analysed "+str(j)+" audio files")
		self.form2.update_message("Detected "+str(k)+" text files")
		self.form2.update_message("Analysed "+str(l)+" video files")
		self.form2.update_progress("Creating Database entries",10)
		self.form2.update_progress("Running clustering algorithm",30)
		subprocess.call(['Rscript','/home/nsk/Desktop/Start/Begin1/Final.r'])
		self.form2.hide()
		self.form3.test()
		self.form3.show()
		#os.system("xdg-open /home/nsk/Desktop/Start/Begin1/Rplots.pdf")
		#os.system("xdg-open /home/nsk/Desktop/Start/Begin1/vis10/index.html")
		




def main():
	app=QtGui.QApplication(sys.argv)
	form=MainClass()
	form.show()
	#web = QWebView()
	#web.load(QUrl("http://google.co.in"))
	#web.show()
	app.exec_()

if __name__=='__main__':
	main()
