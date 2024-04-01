import time
import threading
import multiprocessing


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


start_time = time.time()

for _ in range(10):
    fibonacci(35)

end_time = time.time()
res_time = end_time - start_time
with open('/home/avigdor/projects/advanced_python_itmo_course/hw_4/artifacts/fibonacci_results.txt', 'w') as file:
    file.write(f'Synchronous Execution Time: {res_time} \n')
