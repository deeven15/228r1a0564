def invert_content(dic):
    invert_disc={v: k for k,v in dic.items()}
    return invert_disc
n=int(input("Enter number of values "))
dic={}
for i in range (n):
    key = input("Enter key ")
    value = input("Enter value ")
    dic[key]=value
    print(dic)
print("After invertion")
print(invert_content(dic))