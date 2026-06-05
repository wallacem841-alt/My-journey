x = 29 # this is a global variable
y = 27
def Shenheage(): #This is a function
    print("shenhe is", y) 
    x = "shenhe is awesome" # this is a local variable
    print(x)
    z = "Does this work?" # this only works inside the function
    global k # this makes k global
    k = "this works outside the function" # this is a global variable
# the function ends here
Shenheage() #this calls the function
print(x)
#print(z) # this variable is not defined outside the function and will give an error message (NameError: name 'z' is not defined)
print(k) # this variable is inside a function and it works because of the global keyword