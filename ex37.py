# del
a = [1,2,3]
del a[0]
print a
b = [1,2,3]
del b[1:2]
print b 
# c = [1,2,3]
# del c
# print c


# as 
import random as affection
# another way: import random 
#              affection = random 
#              del random
i = 0
bucket = []
while i < 10:
    i = i + 1
    number = affection.randint(2,5)
    bucket.append(number)
print bucket


# global
def func():
    global x
    print "x is ", x
    x = 2
    print "Change local x to ",x
x = 50 
func()


#try...except
try:
    print input("> ")/input("> ")
except ZeroDivisionError,e:
    print e.message," !!!"
except:
    print "Another kind of errors"

# try...else 
try:
    print input("> ")/input("> ")
except (IOError, ZeroDivisionError),e:
    print e.message," !!!"
except:
    print "Another kind of errors"
else:
    print "no error"

# try...finally
try:
    print input("> ")/input("> ")
except:
    print "error"
finally:
    print "always excute"


# raise
inputValue = input("please input a int data: ")
if type(inputValue) != type(1):
    raise ValueError
else:
    print inputValue
	
try:
    try:
        raise IOError
    except IOError:
        print "inner exception"
        raise 
except IOError:
    print "outter exception"
	
try:
    raise IOError
except IOError:
    print "The error transfer succeeded"


# assert 
try:
    assert input("> ") == input("> ")
except:
    print "The result is False and AssertionError is raised."
else:
    print "The result is True."
	
	
# create your own exception class
class MyException(Exception):
    def __init__(self, message):
        Exception.__init__(self)
        self.message = message
		
if input("please input a num: ") < 10:
    try:
        raise MyException("my exception is raised.")
    except MyException, e:
        print e.message
else:
    raise IOError
	
	
# with 
with open('test.txt') as file:
    print file.read()
# The upper code is equivalent to the following.
try:
    file = open('test.txt')
except:
    pass   # pass doesn't do anything and it's usually used as placeholder.
else: 
    print file.read()
finally:
    file.close()

	
# xrange() is a class that returns a iterable object.
x = xrange(8)
for i in x:
    print x[i]
print x

# range() returns a list
x = range(8)
for i in x:
    print x[i]
print x


# understand yield 
def test_yield(n):
    for i in range(n):
        yield i

for m in test_yield(5):
    print m

# yield Fibonacci sequence 
def fab(max):
    a, b = 0, 1
    while a < max:
        yield b 
        a, b = b, a + b	
for n in fab(5):
    print n
	
	
# break jumps out of the entire for loop
i = 0
while i < 8:
    i = i + 1
    if i == 6:
        break
    else:
        print i
# continue jumps out of this loop
i = 0
while i < 8:
    i = i + 1
    if i == 6:
        continue
    else:
        print i
		
		
# lambda is a tool for constructing callbacks
sum = lambda x, y: x + y 
print sum(5,5)

# it equals to this
# def sum(x,y): 
#     return x + y
# print sum(5,5)

sentence = lambda: "lambda test."
print sentence()

num1 = lambda x, y = 1: x + y
print num1(1)    
print num1(10,10)    


# is 
a = 1
b = 1.0
c = 1
print a is c
print a is b
print id(a)
print id(b)
print id(c)

print 1000 is 10**3  # id 
print 1000.0 == 10**3  # value


# data type
# None
print ''  # it contains a \n
print None == ''
print None == 0
print None == False 
print None == None
print None 


# Escape Sequences
print "\\  \"  \aRing character"
print "\teight indents"
print "\f\v"
print "first\nsecond"
print "first\rsecond"


# Operation symbol
print "+=, -=, *=, /=, //=, %=, **="