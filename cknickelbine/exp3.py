def print2(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" %(arg1, arg2)

def print2_again(arg1, arg2): #this is the same as the uper one just not using *
    print "arg1: %r, arg2: %r" %(arg1, arg2)

def print1(arg1):
    print "arg1: %r" %arg1

def print0():
    print "I got nothin."

def plantane23(arg3, arg4):
    print "arg3: %r, arg4: %r" %(arg3,arg4)

print2 ("Cole", "Thomas")
print2_again ("Cole", "Thomas")
print1 ("First!!!")
print0 ()
plantane23 ('Ohhhhh', 'Baby') #the " " and the ' ' do the same thing
