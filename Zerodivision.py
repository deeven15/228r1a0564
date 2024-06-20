try:
    a = 3
    if a < 4:
        #throws division error for a=3
        b = a/(a-3)
        #throws a name error
        print("value of b",b)
except(ZeroDivisionError,NameError):
    print("Exception handled")
