# this holds the number of cars present
cars = 100
# this says how much space is in a car 
space_in_a_car = 4.0
# this holds the number of drivers
drivers = 30
passengers = 90
# holds number of cars undriven
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today"
print "We can transport", carpool_capacity, "people today"
print "We have", passengers, "to carpool today"
print "We need to put about", average_passengers_per_car, "in each car"
