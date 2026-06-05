x = 'Hello, World!'
y = ' Hello, World! '

print(x[2:5]) #this prints (llo)
print(x[-5:-2]) #this prints (orl)
print(x[:5]) #this prints (hello)
print(x[2:]) #this prints (llo, world!)

print(y.strip()) #this strips the blank spaces in the before and after the text
print(x.replace("o", '@')) #this replace the (o)s with (@)s
#The split() method splits the string into substrings if it finds instances of the separator:
print(x.split(',')) # ['hello', ' world!'] (,) o is the separator
print(x.split('o')) # ['hell', ', w', 'rld!'] (o) is the separator
#Upper and lower
print(x.lower()) # hello, world!
print(x.upper()) # HELLO, WORLD!