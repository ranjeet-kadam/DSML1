import multiprocessing
import math
import time
import sys

sys.set_int_max_str_digits(100000)

def count_fact(number):
    print(f"Comute factorial of {number}")
    result =math.factorial(number)
    return result

if __name__=="__main__":
    numbers =[4000,500,7000,8000]
    start_time = time.time()

    ### Create a multiprocessing pool
    with multiprocessing.Pool() as pool:
        result = pool.map(count_fact,numbers)

        end_time = time.time()

    print(f"Results : {result}")
    print(f"Time taken : {end_time - start_time} seconds")