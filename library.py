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
import random
cards = ['King', 'Queen', 'Jack', '10', '9']
random.shuffle(cards)
for card in cards:
    print(card)