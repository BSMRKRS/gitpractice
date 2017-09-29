def while_loop(limit, increment):
    i = 0
    numbers = []

    while i < limit:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

while_loop(6, 1)


def for_loop(limit, increment):
    for i in range(0, limit, increment):
        print "At the top i is %d" % i
        print "Numbers now: ", range(0, i + increment, increment)
        print "At the bottom i is %d" % (i + increment)
    print "The numbers: "
    for i in range(0, limit, increment):
        print i

for_loop(6, 1)
