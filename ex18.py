def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
    print "arg: %r" % arg1

def print_none():
    print "I got nothing'."

print_two("Ziaja","Emmett")
print_two_again("Ziaja","Emmett")
print_one("First!")
print_none()
