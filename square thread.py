import threading
import time
def f_square(n):
    for i in n:
        time.sleep(0.5)
    print("square = ",n*n)

    def f_cube(m):
        for i in n:
            time.sleep(0.7)
        print("cube = ",n*n*n)
        t1=threading.Thread(traget=f_square,args=())
        t2=threading.Thread(target=f_cube,args=())
        t1.start()
        t2.start()
        t1.join()
