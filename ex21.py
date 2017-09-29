def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract (a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply (a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide (a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "lets do some math with just functions!"

age = add (10, 7)
height = subtract (70, 1)
weight = multiply (15.2, 10)
IQ = divide (300, 5)

print "age: %d, height: %d, weight: %d, IQ: %d" % (age, height, weight, IQ)

print "here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(IQ, 2))))

print "that becomes:" , what, "can you do it by hand?"
