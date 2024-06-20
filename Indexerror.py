a = [1,2,3]
try:
    print("array element",a[1])
    print("array element,",a[7])
except IndexError:
    print("error baby")