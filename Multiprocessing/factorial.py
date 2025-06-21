import multiprocessing
import multiprocessing.pool
import sys
import time
import math

sys.set_int_max_str_digits(100000)

def compute_fact(number):
    print(f"Computing factorial of {number}")
    result = math.factorial(number)
    return result

if __name__ =="__main__":
    numbers = [4000,500,7000,8000]
    start_time = time.time()

    ### Create a multiprocessing pool for the calucation
    with multiprocessing.Pool() as pool:
        result = pool.map(compute_fact,numbers)

    end_time = time.time()


    print(f"Results : {result}")
    print(f"Time taken: {end_time - start_time} seconds")
    
