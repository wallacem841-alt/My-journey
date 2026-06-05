x = 12345

def digits_sum(x):
    if x//10 == 0:
        return x

    z = x % 10

    return z + digits_sum(x//10)

y = digits_sum(x)

print(y)