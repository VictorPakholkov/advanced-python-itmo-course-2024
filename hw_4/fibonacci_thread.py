import time
import threading

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def thread_task():
    fibonacci(35)

start_time = time.time()

threads = []
for _ in range(10):
    thread = threading.Thread(target=thread_task)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

end_time = time.time()

res_time = end_time - start_time
with open('/home/avigdor/projects/advanced_python_itmo_course/hw_4/artifacts/fibonacci_results.txt', 'a') as file:
    file.write(f'Threading Execution Time: {res_time} \n')
