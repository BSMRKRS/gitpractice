def Divisors(n):
    S = 0 #starts the sum count
    for i in range(1,n):
        if n % i == 0: S += i
    return S #take this answer and sen it down to i

def Possible_Pairsrange(low,high):
    k = [Divisors(i) for i in range(low,high + 1)] #k is the divisors in the range plus 1 adding to the count
    pairs = [] #starts the pair count
    for i in range(high - low + 1):
        ind = k[i] #shows its an indefinte value
        if i + low < ind and low <= ind and ind <= high and k [ind - low] == i + low:
            pairs.append([i + low, ind]) #counts up all of the pairs in the range
    return pairs #returns this answer down to the Sum_Pairs

def Sum_Pairs(pairs):
    return sum([sum(pair) for pair in pairs]) #count all of the posisible pairs

ans = Sum_Pairs(Possible_Pairsrange(1, 10000)) #defines the final range of values

print "%s is the number of possible pairs." % ans #prints answer
