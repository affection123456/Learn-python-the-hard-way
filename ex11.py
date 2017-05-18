print "How old are you?",
age = raw_input(">(Input whatever you want) ")

print "How tall are you?",
height = input(">(Please input a number) ")
# 'raw_input()' just print a string but 'input' can process the code.

print "How much do you weigh?",
weight = int(input(">(Please input a number) "))
# "int()" can convert the number which you had printed into integer.
# int(raw_input()) only takes integer.

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)
print "So, you're %s old, %s tall and %s heavy." % (age, height, weight)
# %r is different from %s.