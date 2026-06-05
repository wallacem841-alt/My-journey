Teste = int(input("let's test if your number is prime: "))

divisors = []

for num in range(2,Teste):
    if Teste % num == 0:
        divisors.append(num)

if len(divisors) == 0:
    print(f"{Teste} is a prime number")
else:
    print(f"{Teste} is not a prime number, it's divisors are {divisors}")