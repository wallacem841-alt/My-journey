for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
        print('Jane_doe, Moikaloop, Evelynn')
    elif i % 3 == 0 and i % 5 == 0:
        print('Jane_doe, Moikaloop')
    elif i % 3 == 0 and i % 7 == 0:
        print('Jane_doe, Evelynn')
    elif i % 3 == 0:
        print('Jane_doe')
    elif i % 5 == 0:
        print('Moikaloop')
    elif i % 7 == 0:
        print('Evelynn')
    else:
        print(i)