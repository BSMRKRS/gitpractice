def multiply(c, d):
    print "MULTIPLYING %s * %s" %(c, d)
    return c * d

def add(c, d):
    print "ADDING %s + %s" %(c, d)
    return c + d

field_goals = multiply(12, 2)
three_pointers = add(18, 13)

print "field_goals: %d, three_pointers: %d" %(field_goals, three_pointers)

print "here is a tricky one"

what = add(field_goals, add(field_goals, multiply(three_pointers, 3)))
#why didnt this show the steps?
print "the answer is ", what, "can you do it without a calculator"
