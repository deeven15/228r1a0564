import threading
def cal_fun(h):
    print("thread",h)
t1=threading.Thread(target=cal_fun,args=(10,))
t1.start()