import random

print "Truth Table quiz!"
print "Answer t for True and f for False"
print "Press any key to begin"

raw_input()

questions = [
    {'q': 'not False', 'a': 't'},
    {'q': 'not True', 'a': 'f'},
    {'q': 'True or False', 'a': 't'},
    {'q': 'True or True', 'a': 't'},
    {'q': 'False or True', 'a': 't'},
    {'q': 'False or False', 'a': 'f'},
    {'q': 'True and False', 'a': 'f'},
    {'q': 'True and True', 'a': 't'},
    {'q': 'False and True', 'a': 'f'},
    {'q': 'False and False', 'a': 'f'},
    {'q': 'not (True or False)', 'a': 'f'},
    {'q': 'not (True or True)', 'a': 'f'},
    {'q': 'not (False or True)', 'a': 'f'},
    {'q': 'not (False or False)', 'a': 't'},
    {'q': 'not (True and False)', 'a': 't'},
    {'q': 'not (True and True)', 'a': 'f'},
    {'q': 'not (False and True)', 'a': 't'},
    {'q': 'not (False and False)', 'a': 't'},
    {'q': '1 != 0', 'a': 't'},
    {'q': '1 != 1', 'a': 'f'},
    {'q': '0 != 1', 'a': 't'},
    {'q': '0 != 0', 'a': 'f'},
    {'q': '1 == 0', 'a': 'f'},
    {'q': '1 == 1', 'a': 't'},
    {'q': '0 == 1', 'a': 'f'},
    {'q': '0 == 0', 'a': 't'},
]

random.shuffle(questions)
answers = []

for q in questions:
    a = raw_input(q['q'] + ': ')
    if a == q['a']:
        print "Correct!"
        answers.append(True)
    else:
        print "Incorrect"
        answers.append(False)

score = float(answers.count(True)) / len(answers) * 100

print "You scored: %d%%" % score
