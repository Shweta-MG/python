# Print even number

def main():
    X = int(input('What is X??'))
    if isEven(X):
        print('This is even number')
    else:
        print('This is odd number')

'''
def isEven(n):
    if n % 2 == 0:
        return True
    else: 
        return False
'''
'''
def isEven(n):
    return True if n % 2 == 0  else False
'''

def isEven(n):
    return (n % 2 == 0)

main()