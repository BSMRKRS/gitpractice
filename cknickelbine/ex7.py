print "You are walking in the woods, the trail splits into two paths. L or R?"

path = raw_input ("> ")

if L:
    print "The path starts out easy"
    print "Slowly the path narrows"
    print "You see a dim figure at the end of the path approachin Slowly"
    print "1. Run back up the path"
    print "2. Keep going"

L = raw_input("> ")

if L == "1":
    print "You go back and pick the other path."

if L == "2":
    print "The person is friendly and offers you water."

if R:
    print "The path starts to climp"
    print "You are climbing up a mountain"
    print "you see a huge rock "
    print "1. Climb the rock"
    print "2. Go around the rock"

R = ("> ")

if R == "1":
    print "There is a lake at the top of the rock and you go swimming!!!"

if R == "2":
    print "The path narrows and you fall off the cliff and die."
