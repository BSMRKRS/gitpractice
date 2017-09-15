print "You are walking in the woods, the trail splits into two paths. Left or Right?"

path = raw_input ("> ")

if path == "Left":
    print "The path starts out easy"
    print "Slowly the path narrows"
    print "You see a dim figure at the end of the path approachin Slowly"
    print "1. Run back up the path"
    print "2. Keep going"
else:
    print "Thats not one of the choices idiot"

Run = raw_input("> ")

if Run == "1":
    print "You go back and pick the other path."

elif Run == "2":
    print "The person is friendly and offers you water."
else:
    print "They turn around and chase you into a cave and you starve"

if path == "Right":
    print "The path starts to climp"
    print "You are climbing up a mountain"
    print "you see a huge rock "
    print "1. Climb the rock"
    print "2. Go around the rock"

Climb = raw_input("> ")

if Climb == "1":
    print "There is a lake at the top of the rock and you go swimming!!!"

if Climb == "2":
    print "The path narrows and you fall off the cliff and die."
