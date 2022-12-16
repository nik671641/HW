print('''Press 1 to add a student
      2 to see the list''')

university = {
    'py beginners': {
        'Jake': True,
        'Jane': True,
    },
    'py advanced': {
        'John': True,
        'Marry': True,
        'Peter': True,
    }
}
stud = None
x = university.get('py beginners')
y = university.get('py advanced')
while True:
    add = input('Enter >>>')
    if add == '1':
        addd = input('Тo which group(py beginners/py advanced)?>>>')
        if addd == 'py beginners':
            stud = input('Add student >>>')
            university['py beginners'][stud] = True
        else:
            print(f'{stud} in present')
        if addd == 'py advanced':
            stud = input('Add student >>>')
            university['py advanced'][stud] = True
        else:
            print(f'{stud} in present')

    if add == '2':
        print()
        print('py beginners:')
        print('\n'.join(x))
        print()
        print('py advanced:')
        print('\n'.join(y))
        print()