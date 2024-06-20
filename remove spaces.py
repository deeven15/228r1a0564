import re
a = "my name is deevena kumar, my age is 19"
b = re.sub(r"\s", "", a)  # Here, the second argument is an empty string to remove spaces
print(b)


#remove ., and replace with # symbol
c=re.sub("[ .,]","#",a)
print(c)

#program to seperate numbers from texts and print on new line
d="my age is 19, my rollno is 64"
e=re.findall(r"\d",d)
for x in e:
 print(x)

#program to print vowels
f=re.sub('[aeiouAEIOU]',"",a)
print(f)

#program to print starting letter with m
g=re.findall(r"[nm]\w+",a)
print(g)

#program to print words
h=re.findall(r"\bna\w+",a)
print(h)

#program to print first two letters and last two letters
import re
i="my name is deevena kumar, my age is 19"
j=re.findall(r"\bde\w+na$",i)
print(j)
import re
i = "my name is deevena kumar, my age is 19"
j = re.findall(r"\b(de\w+na)\b", i)
print(j)
#r-raw string,b-first letter,w-whole word,

#to check dollar is present or not
k="my name is deeven,my salary is 92$"
l=re.findall(r"\$",k)
print(l)


