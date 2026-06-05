age = input('give me your age: ')
price = input("give me the product's price: ")

try:
    age = int(age)
    price = float(price)
except ValueError:
    print('Please enter valid numbers for age and price.')
else:
    if age < 18:
        price *= 0.9

print(f'Price: {price:.2f}')