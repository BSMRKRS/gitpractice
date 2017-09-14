print True and True #true
print 1 ==1 or (not("protien" != "peanuts")) #true
print 1 != 0 and 0 != 1 #true
print "corn" != "potatoes" #true
print 1 == 1 and "lime" == "apples" #false


plates = input("Enter a number of plates:")
forks = 22
knives = 24

if plates > forks:
    print "then there will be people who cant eat."

if plates < forks:
    print "thank god!"

plates += 7
if plates <= forks:
    print "everyone can eat."

if plates >= knives:
    print "some people wont be able to cut thier food."
