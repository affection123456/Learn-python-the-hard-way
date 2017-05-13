# cars that we have 
cars = 100
# the basic performance of the cars 
space_in_a_car = 4.0
# people we have 
drivers = 30
# people that we need to transport 
passengers = 90
# the vacant cars 
cars_not_driven = cars - drivers 
# cars which need to be used
cars_driven = drivers
# the ability to transport people
carpool_capacity = cars_driven * space_in_a_car
# the meaning of "average_passengers_per_car" 
average_passengers_per_car = passengers / cars_driven 
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven,"empty cars today."
print "We can transport", carpool_capacity,"people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

the_total_amount = 400
arrears = 300
my_change = the_total_amount - arrears
print "I only have",my_change,"dollars available in total."

# Here I simplify the script.
i = 7
j = 4
x = 7.0
y = 4.0
print i / j, x / y, i / j < x / y