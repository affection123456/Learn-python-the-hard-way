my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74.0*2.54 # centimeters
my_weight = 180.0*0.454 # kilograms
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name   
print "He's %0.1f centimeters tall." % my_height
print "He's %d kilograms heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# This line is tricky, try to get it exactly right.
print "If I add %d, %0.1f, and %d I get %s." % (my_age, my_height, my_weight, my_age + my_height +my_weight)
# Hey!  Please pay attention to what %0.1f %s and %d can do.  
# Don't use %r very frequently.It's just used for debugging.

# The use of '%*f'  If you think it's troublesome, you can change '%*f' to %'s'.
print '%0.1f' % 1.235
print '%3.2f' % 1.235
print '%6.3f' % 1.235
print '%06.3f' %1.235
print '%06.2f' % 1.235
print '%22.12f' % 1.235
print '%-22.12f' % 1.235

# round() can round floating point.
print round(1.0265565564656464888,7) 