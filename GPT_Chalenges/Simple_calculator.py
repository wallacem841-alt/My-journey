test = "87*3+6/2-60"

result = test.replace(" ", "")

test1 = {}

index = 0

for i in range(len(result)):
    try:
        temp = int(result[i])
        if index not in test1:
            test1[index] = ""  # Initialize with an empty string
        test1[index] += str(temp)
    except ValueError:
        index += 1
        test1[index] = result[i]
        index += 1

for i in range(len(test1)):
    if test1[i] == '*' or test1[i] == '/':
        if test1[i] == '*':
            temp = int(test1[i-1]) * int(test1[i+1])
        else:
            temp = int(test1[i-1]) / int(test1[i+1])
        test1.pop(i-1)
        test1.pop(i)
        test1[i+1] = temp

index2 = 0

last_calc = {}

for i in test1:
    last_calc[index2] = test1[i]
    index2 += 1

for i in range(len(last_calc)):
    if last_calc[i] == '+' or last_calc[i] == '-':
        if last_calc[i] == '+':
            temp = int(last_calc[i-1]) + int(last_calc[i+1])
        else:
            temp = int(last_calc[i-1]) - int(last_calc[i+1])
        last_calc.pop(i-1)
        last_calc.pop(i)
        last_calc[i+1] = temp

for i in last_calc:
    print(f"You're result is: {last_calc[i]}")