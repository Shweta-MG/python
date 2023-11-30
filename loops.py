# print this four times

'''
i = 4
while i != 0:
   print ('I am learning and progressing!!', i)
    i -= 1
'''

'''
f = 0
while f < 4:
    print('I am doing it again', f)
    f += 1
'''



# iterate through list of items

'''
for k in [0, 1, 2, 3 , 4]:
    print('I coming from for loop', k)
'''

'''
for k in range(10):
    print ('I am coming from k loops', k)
'''

'''
for _ in range(10):
    print ('I am coming from k loops')

'''

'''
print('I am new \n' * 5, end='')
'''
'''
n = int(input('How many times cat should meow?'))
while n != 0:
    print('I am coming from unser input', n)
    n -= 1
'''


'''
k = int(input('How many times cat should meow?'))

for _ in range(k):
    print('I am coming from for range loops')
'''

'''

k = int(input('How many times cat should meow?'))
if  k <= 0: 
    print ('I am coming from negative loops')
else:
     print ('I am coming from positive loops')

'''

'''
while True:
    k = int(input('How many times cat should meow?'))
    if k > 0:
        break

for k in range(k):
    print('I learn it new', k)
'''


'''
def main():
    k = int(input('How many times cat should meow?'))
    meow(k)
    
def meow(k):
    for _ in range(k):
        print ('I am coming from main functions')

main()
'''

'''

'''

def main():
    k = getNumber()
    meow(k)

def getNumber():
    while True:
        k = int(input('What is k??'))
        if k > 0:
            return k
        

def meow(k):
    for k in range(k):
        print('I am coming from advanced function', k)



main()