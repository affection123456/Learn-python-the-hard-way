tabby_cat = "\tI'm tabbed in."  # \t == eight indents
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat ="""
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat 
print persian_cat 
print backslash_cat
print fat_cat

#the use of some Data Link Escape Character
print "xyz\b\b\bh k  \a"


# \n is different from \r
print "I want something just like this.\rThere's nothing holding me back."
print "I guess you already get the point.\nGood job!"

# Try the code below.
# while True:
#     for i in ["/","-","|","\\","|"]:
#         print "break it with crtl+c", "%s\r" % i,
