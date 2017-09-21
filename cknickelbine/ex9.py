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

cities{'NY'} = 'New York'
cities{'WA'} = 'Seattle'

print '_' * 10
print 'Minnesota abreviation is:' states "[Minnesota]"

print '_' * 10
print 'New York has:' cities[states['New York']]

print '_' * 10
for abrev, city in cities.items()
print "%s state is abbriviated %s and has city %s" %(state, abrev, cities[abrev])

print '_' *10
states = states.get('Texas')

if not state:
    print 'sorry no Texas'

city = cities.get ('TX', 'does not exist')
print "The city for state 'TX' is : %s" %city
