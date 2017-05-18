# open--mode: r--only read, w--write(truncate the original file), a--append 
# "+" == read and write 


from sys import argv
script, filename = argv 

print "We're going to erase %r." % filename 
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename,'w')

print "Truncating the file. Goodbye!"
target.truncate()    # 'truncate()' is not necessary here.

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
# the code down here can do the same
# target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print "And finally, we close it."
target.close()

# Now, you can read the file.
print open(raw_input(">filename ")).read()


# Here is an amazing scipt and you can have try.
# import random
# print open(raw_input(">filename ")).read(random.randint(1,40))