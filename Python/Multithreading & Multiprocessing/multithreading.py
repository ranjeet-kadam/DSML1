import threading
import time

def print_num():
    for i in range(5):
        time.sleep(2)
        print(f"Number is : {i}")

def print_letter():
    for i in "abcede":
        time.sleep(2)
        print(f"Letter : {i}")

### Create a Thread 

t1= threading.Thread(target=print_num)
t2=threading.Thread(target=print_letter)


t=time.time()

### Start the thread
t1.start()
t2.start()

## Wait for the thread complete

t1.join()
t2.join()
finished_time=time.time()-t
print(finished_time)