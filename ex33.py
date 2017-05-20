i = 0 
numbers = []

while i < 6:
    print "At the top i is %d" % i 
    numbers.append(i)
    
    i = i + 1 
    print "Numbers now:", numbers 
    print "At the bottom i is %d" % i 
	
print "The numbers: "

for num in numbers:
    print num

import random
def while_loop(number):
    i = 0
    numbers = []
    print "Let's begin."
    
    while i < number:
        print "At the top i is %d" % i 
        numbers.append(i)
	
        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i 
	
	
        print "The numbers: "
        if len(numbers) == number:
	        for num in numbers:
			    print num
        else:
            print "\t\tWait for it."

while_loop(random.randint(0,10))


# In for-loop, you don't need to define "i".But in while-loop,you have to do that.