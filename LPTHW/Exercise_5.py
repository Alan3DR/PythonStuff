#Exercise 5

my_name = 'Alan Sanchez' #string
my_age = 27  #integer
my_height = 68 #inches
my_weight = 140 #lbs
my_eyes = 'Hazel'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the chocolate milk." % my_teeth

#this line is tricky, try to get it exactly right 
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

print "Testing %r to see what it does" % my_name

# Format Characters:
# %d will format a number for display.
# %s will insert the presentation string representation of the object (i.e. str(o))
# %r will insert the canonical string representation of the object (i.e. repr(o))