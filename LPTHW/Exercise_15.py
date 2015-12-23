#Exercise 15
from sys import argv
#Initiate the script by calling the script and the file:
# python Exercise_15.py ex15_sample.txt
script, filename = argv  

txt = open(filename) #filename is already a string.

print "Here's your file %r:" % filename
print txt.read()
txt.close()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()


#Opening files in Python
#Syntax:
#file_object = open('filename.file_extension','mode')
#	example:  
#	obj = open('ex15_sample.txt', 'r')
#	print obj.read()

#Modes can be:
#'r' when the file will only be read
#'w' for only writing (an existing file with the same name will be erased)
#'a' opens the file for appending; any data written to the file is 
#automatically added to the end. 
#'r+' opens the file for both reading and writing.