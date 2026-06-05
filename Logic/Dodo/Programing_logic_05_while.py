import random

soma = 0
limite = 10

while soma < limite:
    numero = int(input('Digite um numero'))
    soma += numero

print(f'a soma ultrapassou o limite de {limite}. Soma final {soma}')

senha = 1005

tentativa = 0

while tentativa != senha:
    tentativa = int(input("Digite a senha: "))

dataframe = []

num = 0

rannum = int(input('Give me a number: '))

while num < rannum:
    num += 1

    even = num % 2

    if even == 0:
        dataframe.append(num)

print(f'these numbers are even: {dataframe}')

correto = random.randint(1, 20)

tentativa = 0

while tentativa != correto:
    tentativa = int(input("Digite seu número entre 1 e 20: "))
    if tentativa > correto:
        print("muito alto")
    elif tentativa < correto:
        print('muito baixo')
    else:
        print(f'Acerto miseravi, era {correto}')