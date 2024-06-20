import re
text="ab ab cd ef gh"
b = re.findall("xy|gh",text)
print(b)