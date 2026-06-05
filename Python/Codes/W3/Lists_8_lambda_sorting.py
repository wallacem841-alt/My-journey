data = [('Alice', 30), ('Bob', 25), ('David', 35), ('Carla', 20), ('Dodo', 21), ('wallace', 29), ('joui',25)]
data.sort(key=lambda x: x[1])

print(data)

data.sort(key=lambda x: x[0])

print(data)

data.sort(key=lambda x: len(x[0]))

print(data)

employees = [('Alice', 'Engineering'), ('Bob', 'HR'), ('Alex', 'Engineering'), ('Bob', 'Engineering')]

employees.sort(key=lambda x: (x[1], x[0]))

print(employees)  # Output: [('Alex', 'Engineering'), ('Alice', 'Engineering'), ('Bob', 'Engineering'), ('Bob', 'HR')]
