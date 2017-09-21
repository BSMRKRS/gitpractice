states = {
    'Minnesota': 'MN',
    'New York': 'NY',
    'Wisconsin': 'WI'
}

Cities = {
    'MN': 'Minneapolis',
    'MI': 'Detroit',
    'OK': 'Norman'
}

Cities['NY'] = 'New York',
Cities['WA'] = 'Seattle'

print '_' * 10
print 'Minnesota abreviation is:', states['Minnesota']

print '_' * 10
print 'New York has:', Cities[states['New York']]

print '_' * 10
for abbrev, city in Cities.items():
    print "%s state is abbriviated %s and has city %s" %(states, abbrev, Cities[abbrev])

print '_' *10
states = states.get('Texas')

if not states:
    print 'sorry no Texas'

city = Cities.get ('TX', 'does not exist')
print "The city for state 'TX' is : %s" %city
