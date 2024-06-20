def fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

# Input number of terms from user
n = int(input("Enter the number of terms in the Fibonacci sequence: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    fib_sequence = fibonacci_sequence(n)
    print("Fibonacci sequence:")
    for num in fib_sequence:
        print(num, end=" ")
