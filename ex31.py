print "You enter a dark room with two doors.  Do you go through door #1, door #2, or door #3.141592653589793? "

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake.  What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    print "x. Return to Dimension X."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off.  Good job!"
    elif bear == "2":
        print "The bear eats your legs off.  Good job!"
    elif bear == "x":
        print "Tell Krang I said 'hello.'"
    else:
        print "Well, doing %s is probably better.  Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."
    print "z. Eat the pizza that Splinter left out for you."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello.  Good job!"
    if insanity == "z":
        print "Cowabunga! It's turtle time!"
    else:
        print "The insanity rots your eyes into a pool of muck.  Good job!"

elif door == "3.141592653589793":
    print "You're so irrational."

else:
    print "You stumble around and fall on a knife and die.  Good job!"
