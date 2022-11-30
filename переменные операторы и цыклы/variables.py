print(""" Choose an action:
    1. Show tasks
    2. Add tasks
    3. Remove tasks
    4. Clear tasks   
    5. Output
""")
tasks = ['Learn Python',
         'Become a dev',
         'Become a Millionaire']
while True:
    # ###############  INTERACTION  #######################

    ne_tasks = input('Enter :')

    if ne_tasks == '1':
        pass
    elif ne_tasks == '2':
        new_tasks = input('Add tasks :')
        if new_tasks not in tasks:
            tasks.append(new_tasks)
    if ne_tasks == '3':
        index = int(input('Deiete: '))
        tasks.pop(index)
    if ne_tasks == '4':
        tasks.clear()
    if ne_tasks == '5':
        break

    # ###############  INTERACTION  #######################

    # ###############  PRINT THE TASKS  ###################
    print('TODO List (', len(tasks), '):')
    for i in range(len(tasks)):
        print('\t', i, '>', tasks[i])

    # ###############  PRINT THE TASKS  ###################
