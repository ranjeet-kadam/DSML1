## Multiprocessing with process pool executor

from concurrent.futures import ProcessPoolExecutor
import time

def square(num):
    time.sleep(1)
    return f"Square is : {num*num}"

numbers = [1,2,3,6,4,86,32]

t = time.time()

if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=3) as executor:
        time.sleep(1)
        results =executor.map(square,numbers)

    print(*results,sep="\n")
    finished_time = time.time()-t
    print(finished_time)

