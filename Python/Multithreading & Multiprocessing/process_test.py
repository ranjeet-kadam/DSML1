import multiprocessing
import time

def square_num():
    for i in range(5):
        time.sleep(1)
        print(f"The Square is : {i*i}")

def cube_num():
    for i in range(5):
        time.sleep(1.5)
        print(f"The Cube is : {i*i*i}")

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=square_num)
    p2 = multiprocessing.Process(target=cube_num)

    t = time.time()

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    # Uncomment below if you want to run again after the processes finish
    # square_num()
    # cube_num()

    finished_time = time.time() - t
    print(f"Finished in {finished_time:.2f} seconds")
