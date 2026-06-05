#x = "I am a "god"" #this gives out an error (SyntaxError: invalid syntax)
y = "I am \"Humble\"" #this goes out correctly

#print(x) # this gives error (NameError: name 'x' is not defined)
print(y)

#other Escape caracters

x = 'I\'m awsome' #\'
q = 'we play honkai\\LOL' #\\
w = 'this is a line.\nthis is another line' #\n
e = 'Hello,12345 \rWorld!' #ths overwrites everything before \r like this (World!12345)
r = "Hello\tWorld!" #gives space (Hello   World!)
t = "Hello \bWorld!" # this takes space (HelloWorld!)
u = "\110\145\154\154\157" #octal value (Hello) = \ooo
i = "\x48\x65\x6c\x6c\x6f" #Hex value (Hello) = \xhh

print(x)
print(q)
print(w)
print(e)
print(r)
print(t)
print(u)
print(i)

'''In Python, \f represents a form feed character.
The form feed character is a control character used to start a new page in printed documents
or to advance the paper to the next page in a printer. In modern computing, its usage is less common,
but it can still be employed in specific contexts.
For example, you might encounter \f in strings that are used for formatting or printing purposes.
Here's a simple example:'''
print("Hello\fWorld") #Hello♀World
