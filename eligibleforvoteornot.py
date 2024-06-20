def check_eligibility(age):
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")

# Taking age as input
age = int(input("Enter your age: "))
check_eligibility(age)
