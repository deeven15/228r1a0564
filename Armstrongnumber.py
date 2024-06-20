def is_armstrong_number(num):
    # Calculate the number of digits
    num_digits = len(str(num))
    # Calculate the sum of the nth power of each digit
    sum_of_digits = sum([int(digit)**num_digits for digit in str(num)])
    # Check if the sum is equal to the original number
    return sum_of_digits == num

# Input number from user
num = int(input("Enter a number: "))

if is_armstrong_number(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
