from sys import argv 

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename 
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()


# I make the progress easier.
x = raw_input("> ")
y = open(x)
print y.read()    # "open()" can open many things, such as .txt, .py, and so on.
y.close()    # This step is necessary after you edited the file.


# If you are too lazy, you can try the code below.
print open(raw_input(">filename: ")).read()