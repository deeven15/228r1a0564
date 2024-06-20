try:
    a=int(input("Enter the a values"))
    b=int(input("Enter the b values"))
    c=a/b
    print("value of c:",a+b)
    x=[1,2,3,4]
    print(x[5])
except Exception:

#except ZeroDivisionError:
  #print(" a value is not mentioned")
  print("After exception")
except NameError:
    print(" a value is not mentioned")
except ValueError:
    print("Value error")
except IndexError:
    print("Array index out of bounds")
except KeyError:
    print("Key Error")
except IOError:
    print("file input or output error")