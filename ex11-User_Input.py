#raw_input does not try to interpret the data entered, so its safer

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So you are %s old, %s tall and %s heavy" % (age, height, weight)