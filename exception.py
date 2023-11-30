'''
try:
    x = int(input('What is X??'))
    print(f'x is {x}')
except ValueError:
    print('Invaliddd Input')
'''


#print statement is moved
'''
try:
    x = int(input('What is X??'))

except ValueError:
    print('Invaliddd Input')
else:
    print(f'x is {x}')
'''


#using while loop - on invalid input loop will start again
'''
while True:
    try:
        x = int(input('What is X??'))
    except ValueError:
        print('Invaliddd Input')
    else:
        break
        

print(f'x is {x}')
'''



#little less codes
'''
while True:
    try:
        x = int(input('What is X??'))
        break
    except ValueError:
        print('Invaliddd Input')     
        

print(f'x is {x}')
'''



#main function
def main():
    x =  get_int()
    print(f'x is {x}')


def get_int():
    while True:
        try:
            x = int(input('What is X??'))
            break
        except ValueError:
            print('Invaliddd Input')  
    return x  
  

main()