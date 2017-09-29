#Solving euler theorem 16

#This will be the given original problem to break down every number and add together
result = 2 ** 1000

#string meaning every individual digit of orginal problem is divided or...
#thought as a stand alone digit
string_result = str(result)

#sum of the number strung out (adding zero)
Sum = 0

#adding of every individual number + 0 (defined as sum)
for number in string_result:
    Sum = Sum + int(number)

#give the result by printing it or showing it
#this is the only command line you should see when showing the file
print Sum
