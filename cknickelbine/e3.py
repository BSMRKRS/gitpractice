from decimal import Decimal, localcontext

def i(): #defines i as the number
    total = 0
    for x in range(1,100): #first 100 numbers in the sequence
        print x
        with localcontext() as ctx:
            ctx.prec = 105 #has to be 105 otherwise it isnt precise enough
            if len(str(Decimal(x).sqrt())) == 1: #square rt of the number
                total+=0
            else: #prints all of the numbers and then adds up the first 100
                a = sum([int(i) for i in str(Decimal(x).sqrt())[2:101]])+int(str(Decimal(x).sqrt())[0])
                total+=a
    return total
print i()
