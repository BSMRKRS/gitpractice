import math

divisors = []
pairs = 0
totalPairs = 0


#finds the factorial of a number n

primeFactors = []
def factorial(n):
    d = 1
    for i in range(1,n+1):
        d = i * d
    return d
# determines if a number is prime
def isPrime(numb):
    j = 2
    while True:
        if numb % j == 0 and j != numb:
            return(False)
        elif numb % j == 0 and j == numb:
            return(True)
        else:
            j += 1
#testedit

# finds the prime divisors of a number n and appends them to a list primeFactors
def findDenom(numb):
    print "finding factors: %d" % numb
    i = 2
    while True:
        if numb % i == 0:
            denom = numb / i
            print "numb: %d, i: %d, denom: %d" % (numb,i,denom)
            locI = isPrime(i)
            locDenom = isPrime(denom)
            if locI and locDenom:
                primeFactors.append(denom)
                primeFactors.append(i)
                return()
            elif locDenom:
                primeFactors.append(denom)
                findDenom(i)
                return()
            elif locI:
                primeFactors.append(i)
                findDenom(denom)
                return()
            else:
                findDenom(i)
                findDenom(denom)
                return()
        else:
            i += 1
# creates a list of all the primes under  100
primeFactorsSorted = []
for i in range(2,100):
    if isPrime(i):
        primeFactorsSorted.append([i,0])

# takes the list of prime divisors (primeFactors) and converts it into a prime factorization in list primeFactorsSorted
def sortPrimeFactorization():
    for i in range(len(primeFactors)):
        for j in range(len(primeFactorsSorted)):
            if primeFactors[i] == primeFactorsSorted[j][0]:
                primeFactorsSorted[j][1] += 1
                j = (len(primeFactorsSorted))

# finds the total number of combinations of primes possible when split in two from a prime factorization
# this is the number of divisors of a number
def combinationsOfPrimes():
    a = 1
    for i in range(len(primeFactorsSorted)):
        b = primeFactorsSorted[i][1] + 1
        a = a * b
    print a

"""
This function iterates through all possible splits of a divisor prime factorization, and checks how many divisors each divisors contains
"""
def divisorsOfDivisors():
    global pairs
    for a in range(primeFactorsSorted[0][1] + 1):
        for b in range(primeFactorsSorted[1][1] + 1):
            for c in range(primeFactorsSorted[2][1] + 1):
                for d in range(primeFactorsSorted[3][1] + 1):
                    for e in range(primeFactorsSorted[4][1] + 1):
                        for f in range(primeFactorsSorted[5][1] + 1):
                            for g in range(primeFactorsSorted[6][1] + 1):
                                for h in range(primeFactorsSorted[7][1] + 1):
                                    for i in range(primeFactorsSorted[8][1] + 1):
                                        for j in range(primeFactorsSorted[9][1] + 1):
                                            for k in range(primeFactorsSorted[10][1] + 1):
                                                for l in range(primeFactorsSorted[11][1] + 1):
                                                    for m in range(primeFactorsSorted[12][1] + 1):
                                                        for n in range(primeFactorsSorted[13][1] + 1):
                                                            for o in range(primeFactorsSorted[14][1] + 1):
                                                                for p in range(primeFactorsSorted[15][1] + 1):
                                                                    for q in range(primeFactorsSorted[16][1] + 1):
                                                                        for r in range(primeFactorsSorted[17][1] + 1):
                                                                            for s in range(primeFactorsSorted[18][1] + 1):
                                                                                for t in range(primeFactorsSorted[19][1] + 1):
                                                                                    Right = (a + 1) * (b + 1) * (c + 1) * (d + 1) * (e + 1) * (f + 1) * (g + 1) * (h + 1) * (i + 1) * (j + 1) * (k + 1) * (l + 1) * (m + 1) * (n + 1) * (o + 1) * (p + 1) * (q + 1) * (r + 1) * (s + 1) * (t + 1)
                                                                                    Left = (primeFactorsSorted[0][1] - a + 1) * (primeFactorsSorted[1][1] - b + 1) * (primeFactorsSorted[2][1] - c + 1) * (primeFactorsSorted[3][1] - d + 1) * (primeFactorsSorted[4][1] - e + 1) * (primeFactorsSorted[5][1] - f + 1) * (primeFactorsSorted[6][1] - g + 1) * (primeFactorsSorted[7][1] - h + 1) * (primeFactorsSorted[8][1] - i + 1) * (primeFactorsSorted[9][1] - j + 1) * (primeFactorsSorted[10][1] - k + 1) * (primeFactorsSorted[11][1] - l + 1) * (primeFactorsSorted[12][1] - m + 1) * (primeFactorsSorted[13][1] - n + 1) * (primeFactorsSorted[14][1] - o + 1) * (primeFactorsSorted[15][1] - p + 1) * (primeFactorsSorted[16][1] - q + 1) * (primeFactorsSorted[17][1] - r + 1) * (primeFactorsSorted[18][1] - s + 1) * (primeFactorsSorted[19][1] - t + 1)
                                                                                    if Right == Left:
                                                                                        pairs += 1

# This takes an input of a number n and factorizes it
n = factorial(int(raw_input()))
print n
findDenom(n)
sortPrimeFactorization()
divisorsOfDivisors()
pairs = pairs / 2
print "%d" % pairs

"""
for u in range(primeFactorsSorted[20][1] + 1):
    for v in range(primeFactorsSorted[21][1] + 1):
        for w in range(primeFactorsSorted[22][1] + 1):
            for y in range(primeFactorsSorted[23][1] + 1):
                for x in range(primeFactorsSorted[24][1] + 1):
                    for z in range(primeFactorsSorted[25][1] + 1):
                        Right = (a + 1) * (b + 1) * (c + 1) * (d + 1) * (e + 1) * (f + 1) * (g + 1) * (h + 1) * (i + 1) * (j + 1) * (k + 1) * (l + 1) * (m + 1) * (n + 1) * (o + 1) * (p + 1) * (q + 1) * (r + 1) * (s + 1) * (t + 1) * (u + 1) * (v + 1) * (w + 1) * (y + 1) * (x + 1) * (z + 1)
                        Left = (primeFactorsSorted[0][1] - a + 1) * (primeFactorsSorted[1][1] - b + 1) * (primeFactorsSorted[2][1] - c + 1) * (primeFactorsSorted[3][1] - d + 1) * (primeFactorsSorted[4][1] - e + 1) * (primeFactorsSorted[5][1] - f + 1) * (primeFactorsSorted[6][1] - g + 1) * (primeFactorsSorted[7][1] - h + 1) * (primeFactorsSorted[8][1] - i + 1) * (primeFactorsSorted[9][1] - j + 1) * (primeFactorsSorted[10][1] - k + 1) * (primeFactorsSorted[11][1] - l + 1) * (primeFactorsSorted[12][1] - m + 1) * (primeFactorsSorted[13][1] - n + 1) * (primeFactorsSorted[14][1] - o + 1) * (primeFactorsSorted[15][1] - p + 1) * (primeFactorsSorted[16][1] - q + 1) * (primeFactorsSorted[17][1] - r + 1) * (primeFactorsSorted[18][1] - s + 1) * (primeFactorsSorted[19][1] - t + 1) * (primeFactorsSorted[20][1] - u + 1) * (primeFactorsSorted[21][1] - v + 1) * (primeFactorsSorted[22][1] - w + 1) * (primeFactorsSorted[23][1] - y + 1) * (primeFactorsSorted[24][1] - x + 1) * (primeFactorsSorted[25][1] - z + 1)
                        if Right == Left:
                            print "%d, %d, %d, %d" % (i,j,k,l)
                            pairs += 1

"""
