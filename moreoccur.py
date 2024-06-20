import re
text = "welcome to cmrec"
b=re.findall("co*",text)
print(b)

#*- 0 or more ocurrances
#+- 1 or more ocurrances
#?-0 or 1 occurance