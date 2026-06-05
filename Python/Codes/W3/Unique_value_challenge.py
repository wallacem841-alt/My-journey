array = [17, 42, 56, 23, 17, 89, 42, 23, 56, 74, 99, 89, 74, 133, 101, 133, 101, 67, 58, 58, 27, 67, 27, 13, 88, 13, 88, 34, 34, 92, 65, 92, 65, 47, 112, 47, 77, 112, 77, 33, 120, 39, 33, 39, 11, 140, 11, 55, 140, 55, 121]

temporary_array1 = []

temporary_array2 = []

final_array = []

for x in range(len(array)):
    if array[x] in temporary_array1:
        temporary_array2.append(array[x])
    else:
        temporary_array1.append(array[x])

for x in range(len(array)):
    if array[x] in temporary_array2:
        continue
    else:
        final_array.append(array[x])

print(final_array)