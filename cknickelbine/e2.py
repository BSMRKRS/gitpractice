import time
begin = time.time()
#turned the trangle into a number
number = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

number = number.strip().split('\n')
#splits the number into strands and then into intigers
for j in range(1, len(number)):
    number[j] = number[j].strip().split(' ')
    number[j] = [int(x) for x in number[j]]
#defines the first number where the program should start as 75
number[0] = [75]
#for all of the lines 0-14 stry i
for k in range(len(number[j]) -1, -1, -1):
    for i in range(0,k):
        #for number take one less than it add up the ajacent numbers
        #adds up all of the biggest numbers and sets that as j k
        number[k - 1][i] += max(number[k][i], number[k][i + 1])
#take the number and print the answer
print number[k][i]

elapsed = (time.time() - begin)

print elapsed
