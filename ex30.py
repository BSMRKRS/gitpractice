people = 30
cars = 40
trucks = 15

# In the event that the number of cars is greater than the number of people...
if cars > people:
    print "We should take the cars."
# In the event that the number of cars is less than the number of people...
elif cars < people:
    print "We should not take the cars."
# Otherwise (the number of cars is equal to the number of people)...
else:
    print "We can't decide."

# In the event that the number of trucks is greater than the number of cars...
if trucks > cars:
    print "That's too many trucks."
# In the event that the number of trucks is less than the number of cars...
elif trucks < cars:
    print "Maybe we could take the trucks."
# Otherwise (the number of trucks is equal to the numbe rof cars)...
else:
    print "We still can't decide."

# In the event that the number of people is greater than the number of trucks...
if people > trucks:
    print "Alright, let's just take the trucks."
# Otherwise (the number of trucks is greater than the number of people, or
# the number of trucks is equal to the number of people)...
else:
    print "Fine, let's stay home then."
