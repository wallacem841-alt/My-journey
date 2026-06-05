def powers_of_2(list, x):
    if x <= 0:
        list.append(1)
        return
    
    powers_of_2(list, x - 1)

    list.append(2**x)

    return


result = []

powers_of_2(result, 4)

print(result)