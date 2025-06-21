from concurrent.futures import ThreadPoolExecutor
import time

def num(numbers):
    time.sleep(1)
    return f"Numbers are : {numbers}"

number = [1,2,4,5,67,98,6,5,4]
t=time.time()

with ThreadPoolExecutor (max_workers=3) as executor:
    time.sleep(1)
    result =executor.map(num,number)

#for results in result:
    #print(results)
print(*result, sep="\n") ## unpacking the list and print in the new line.

finished_time = time.time()-t
print(finished_time)