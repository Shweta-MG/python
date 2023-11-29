'''
students = ['Olivia', 'Tetiana', 'Camilla', 'Camila']

for i in range(len(students)):
    for k in range(len(students[i])):
        print(k+1, students[i][k])
    print(i+1, students[i])
'''

'''
#Object in JS is called dict (Dictionary) in python
student_grades = {
    'Alice': 95,
    'Bob': 89,
    'Charlie': 75,
    'David': 92,
    'Eva': 88
}
#This will fives only keys and values
for i in student_grades:
    print(i , student_grades[i], sep=', ' )
'''
'''
students = [
    {"name": "Hermoine", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for i in students:
    print( i['name'], i['house'], sep=', ')

'''

#print rows
'''
def main():
    rows(4)
    columns(7)

def rows(width):
    print('??  ' * width)

def columns(height):
    for _ in range(height):
     print('CC  cc')

main()
'''

#print a square
def main():
    square_size = int(input('How big is the square??'))
    print_square(square_size)

def print_square(size):
    for i in range(size):
        for k in range(size):
            print('#', end='')
        print()

main()
