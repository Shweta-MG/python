'''
try:
    x = int(input('What is X??'))
    print(f'x is {x}')
except ValueError:
    print('Invaliddd Input')
'''



try:
    x = int(input('What is X??'))

except ValueError:
    print('Invaliddd Input')
else:
    print(f'x is {x}')