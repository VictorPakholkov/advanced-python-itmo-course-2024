import time
import threading
import multiprocessing

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def process_task():
    fibonacci(35)

start_time = time.time()

processes = []
for _ in range(10):
    process = multiprocessing.Process(target=process_task)
    process.start()
    processes.append(process)

for process in processes:
    process.join()

end_time = time.time()
res_time = end_time - start_time
with open('/home/avigdor/projects/advanced_python_itmo_course/hw_4/artifacts/fibonacci_results.txt', 'a') as file:
    file.write(f'Multiprocessing Execution Time: {res_time} \n')