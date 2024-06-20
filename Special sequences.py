import re
#\A is used to print first character of string

a = " my name is deeven, my age is 18"
b = re.findall(r"\A my",a)
j = re.findall(r"\s",a) #it is used to how many spaces are available in the given string sentence
k =re.findall(r"\S",a)#it will print without spaces
m=re.findall(r"\w",a)#it will print 0-9,a-z,A-Z
n=re.findall(r"\W",a)# Except 0-9,a-z,A -Z it will print everything
print(b)
print(j)
print(k)
print(m)
print(n)

#\d for digits
c="my name is leonardo dicaprio, my age is 18"
d=re.findall(r"\d",c) #it will display only digits
l=re.findall(r"\D",c) #it will display everything except digits
print(d)
print(l)

#\D
e="i am fan of titanic"
f=re.findall(r"\D",e)
g=re.findall(r"\w",e) #without whitespaces
i=re.findall(r"titanic\Z",e) #available at last or not
h=re.findall(r"\B",e)
o=re.findall(r"an\b",e) #it prints specific characters  \b-first-first character \B-last-last character


print(f)
print(g)
print(h)
print(i)
print(o)