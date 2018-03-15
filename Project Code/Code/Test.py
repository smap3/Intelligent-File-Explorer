from Database import Database

a=Database("Test")
a.set_collection("Files")
key_string="/home/nsk/Test.txt"
value_string="/home/nsk/Test.mp3"
key_string=key_string.replace(".",";")
value_string=value_string.replace(".",";")
a.add_entry(key_string,value_string)
print "Testing result:"
b=a.search_Files(key_string).replace(";",".")
print b
a.close()
