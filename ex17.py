from sys import argv
from os.path import exists

script, from_file, to_file = argv 

print "Copying from %s to %s" % (from_file, to_file)

# We could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)   # return the length of the string

print "Does the output file exist? %r" % exists(to_file)   # return True or False
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')  # pay attention to the mode
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()


# I can write the code into one line!
# open('copied.txt','w').write(open('test.txt').read())