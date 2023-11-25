x = input('What is x?')

match x:
    case 'Mor':
        print('Mor laver mad.')
    case 'Far':
        print('Far spiller hele tiden.')
    case 'Søn':
        print('Han leger.')
    case _:
        print('Jeg ved det ikke, hvad laver de?')
