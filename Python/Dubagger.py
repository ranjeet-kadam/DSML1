# def square(n):
#     for i in range(3):
#         yield i**2

# for i in square(3):
#     print(i)

def fibonacci_series(limit):
    a,b=0,1

    while a<limit:
        yield a
        a,b =b,a+b

for num in fibonacci_series(10):
    print(num)