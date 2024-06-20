import threading
import time

def square(n):
    print("square of numbers:")
    for i in n:
        time.sleep(0.2)
        print("square of number is", i * i)

def cube(m):
    print("cube of numbers:")
    for i in m:
        time.sleep(0.2)
        print("cube of number is", i * i * i)

# Start time
start_time = time.time()

l = [1, 2, 3, 4, 5]

# Create threads
t1 = threading.Thread(target=square, args=(l,))
t2 = threading.Thread(target=cube, args=(l,))

# Start threads
t1.start()
t2.start()

# Wait for both threads to complete
t1.join()
t2.join()

# End time
end_time = time.time()

print("time taken to execute two functions:", end_time - start_time)
