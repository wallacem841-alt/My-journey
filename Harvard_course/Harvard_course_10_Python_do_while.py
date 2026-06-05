while True:
    n = input("Give me and integer")

    try:
        n = int(n)
    except:
        n = -1

    if n > 0:
        break

    print(n)

print(n)