import re
text="welcome to cmrec kandlakoya"
b=re.findall("[^cmr]",text)
print(b)
b=re.sub("[^aeiou]","#",text)
print(b)

