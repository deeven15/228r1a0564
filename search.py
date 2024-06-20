#in search function characters are searched at any place
#if both characters are same it will only search first character ex:"my"
import re
a="my name is deevena kumar"
b=re.search("deeven",a)
#print(b)

#findall function
c="my name is deevena kumar,my age is 19"
d=re.findall("my",a)
#print(d)

#split function
#it will remove the given character
#in place of character output will give ,
e="my name is deevena kumar"
f=re.split("deeven",a)
#print(f)

#sub function - it is used to replace string
g="my name is deevena kumar , i will get outstanding"
h=re.sub("deeven","leonardo",a)
print(h)
