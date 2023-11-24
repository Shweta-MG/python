#print('Hello world')
#print('This is my very first python codes running here!!! Yeepieeee')


#Ask user your name
# 
#name = input('What\'s your name??').strip().title()
#name = name.strip()
#name = name.capitalize() #capitalised first letter
#name = name.title()

#Print user name
#print('hello')
#print(name)



#print with updated end condition
#print('hello!! ', end='')
#print(name)

#print(f'Hello !! {name}')

# a calculator programme
'''
x = float(input('What is X?'))
y = float(input('What is Y?'))
z = round(x + y)
'''
 
#print(z)
'''
XX = float(input('What is XX??'))
z = round (3.9 * XX * (XX + 1 ) - 5 )

ZZ = (3.9 * XX * (XX + 1 ) - 5 )

print(z)
print(ZZ)
'''



'''
# programme to convert European floor number to US floor numbre in elevator
Eur = input('What is the floor number?')
UsF = int(Eur) + 1
print('US floor number will be ', UsF )
'''


'''
d = input('What is d??')
if d == 5:
    print('D is 5.', d)
    if d < 5:
        print('d is less than 5', d)
        if d > 5:
             print('d is greater than 5', d)
'''

'''
x = float(input('What is x?'))
y = float(input('What is y?'))
z = round(x + y)
ZZ = x + y

print(z)
print(f'{ZZ: .2f}')
print(round(ZZ, 2))
'''

'''
def hello(to = 'World'):
    print('Hello', to)

hello()

Name =  input('What is your name??')
hello(Name)
'''



def plus(x = 9, y = 10):
    print(x + y)

plus()

x = int (input('What is x?'))
y = int (input('What is y??'))
plus(x, y)
