colors = {'red', 'green', 'yellow'}
fruit = {'pears', 'limes', 'oranges'}
people = {'billy', 'Grizz', 'Angel'}
change = {'1 Dime', '3 Quarters'}

for colors in colors:
    print "This %s is the color we are painting with" %colors

for fruit in fruit:
    print "We are eating %r today for lunch" %fruit

for name in people:
    print "I sent %r to help you with homeowork today" %name

for i in change:
    print "I got %r" %i

elements = {}

for i in range(0, 11):
    print "Add %d to the list" %i
