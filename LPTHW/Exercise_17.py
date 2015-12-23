#Exercise 17
from sys import argv
from os.path import exists
#script, from_file, to_file = argv

from_file = raw_input('What file do you want to copy?\n> ')
to_file = raw_input('Where do you want to copy to?\n> ')

#print "Copying from %s to %s" % (from_file, to_file)

#we could do these two on one line too, how?
#in_file = open(from_file)
#indata = in_file.read()

	#indata= open(from_file).read()

#print "The input file is %d bytes long" % len(indata)
#print "Does the output file exist? %r" % exists(to_file)
#print "Ready, hit RETURN to continue, CTRL-C to abort."
#raw_input(> )

#out_file = open(to_file, 'w')
#out_file.write(indata)

	#out_file = open(to_file, 'w').write(indata)


out_file = open(to_file, 'w').write(open(from_file).read())
#print "Alright, all done"

#out_file.close()
#in_file.close()
