'''
import random

coin = random.choice(['Head', 'Tail'])

print(coin)
'''

#Only needed function is imported
'''
from random import choice
options = ['Head', 'Tail']
coin =  choice(options)
print(coin)
'''

#print random number
'''
import random
printRandom = random.randint(0, 90)
print(printRandom)
'''


#shuffle list of something
#shuffle does the a new shuffled list
'''
import random
cards = ['King', 'Queen', 'Jack', '10', '9']
random.shuffle(cards)
for card in cards:
    print(card)
'''

#system argument
'''
import sys
try:
    print('Hello, My name is ', sys.argv[1])
except IndexError:
    print('Few argument missing')
'''

'''
import sys
if len(sys.argv) < 2:
    print('Too few argument')
elif len(sys.argv) > 2:
    print('Too many argument')
else:
    print('Hello, My name is ', sys.argv[1])
'''

# try and except
'''
import sys
if len(sys.argv) < 2:
    sys.exit('Too few argument')
elif len(sys.argv) > 2:
    sys.exit('Too many argument')

print('Hello, My name is ', sys.argv[1])
'''


#packages
# run in terminal 'pip install cowsay'
import cowsay
import sys
'''
if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])
'''



if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])