import _thread
import time

def name(n):
    time.sleep(0.5)
    print("my name is", n)

def country(m):
    time.sleep(0.5)
    print("i live in", m)

r = time.time()

_thread.start_new_thread(name, ("deeven",))
_thread.start_new_thread(country, ("canada",))

# Adding a delay to allow threads to finish
time.sleep(1)

print("time taken to execute two functions", time.time() - r)
