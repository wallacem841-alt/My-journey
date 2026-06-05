x = 29
y = 'I am'
z = 'years old'
k = 'I am {} years old'
a = y + ' ' + str(x) + ' ' + z #This combines the variables by turning x into string
# we can also combine strings and numbers by using the .format() method!
b = k.format(x) #this combines the variables using .format() 

print(a) 
print(b)

# .format works as a list
MSG = 'I sold {} units on the day {}, that amounts to {}$.'

Nsold = 35
Price = 100
Day = '11/01/2024'

Full_MSG = MSG.format(Nsold, Day, Nsold + float(Price))

print(Full_MSG)

# you can change the index of the list

MSG2 = 'I sold {2}$ on the day {1}, it was {0} units.' 

Full_MSG2 = MSG2.format(Nsold, Day, Nsold + float(Price))

print(Full_MSG2)