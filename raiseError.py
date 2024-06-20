try:
    raise NameError("HI THERE")
except NameError:
    print("Exception handles")
    raise #to determine whether exception raised or not