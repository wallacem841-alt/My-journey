x = 10
y = 1

if x == y:
    print("x = y")
else:
    print('x != y')

age = 20

if age >= 16 and age <= 65:
    print('Obrigatório votar')
else:
    print('Menos escravo')

fee = 0

if age <= 12:
    fee = 10
elif age >= 13 and age <=17:
    fee = 15
elif age >= 18:
    fee = 20
else:
    print('invalid age')

print(f'Fee = ${fee}')  