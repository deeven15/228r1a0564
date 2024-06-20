import re
text="ab ab cd ef gh"
b = re.findall("ab{1,2}",text)
print(b)
c = re.findall(".a",text)
print(c)
#'''z = re.sub("\s","#",text)
#print(z)'''