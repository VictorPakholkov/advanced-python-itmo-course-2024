import os
import math
import time
import concurrent.futures
import logging

logging.basicConfig(filename='integrate_log.txt', level=logging.DEBUG, format='%(asctime)s - %(message)s')

def integrate_worker(func, start, end, n_steps):
    logging.debug(f'Starting task: func={func}, start={start}, end={end}, n_steps={n_steps}')
    dx = (end - start) / n_steps
    total = 0
    for i in range(n_steps):
        x = start + i * dx
        total += func(x)
    return total * dx

def integrate(func, start, end, n_steps, n_jobs=1):
    if n_jobs == 1:
        return integrate_worker(func, start, end, n_steps)

    chunk_size = n_steps // n_jobs
    chunks = [(func, start + i * chunk_size, start + (i + 1) * chunk_size, chunk_size) for i in range(n_jobs)]

    with concurrent.futures.ThreadPoolExecutor(max_workers=n_jobs) as executor:
        results = executor.map(integrate_worker, *zip(*chunks))

    return sum(results)

def run_integration(n_jobs, use_processes=False):
    start_time = time.time()

    if use_processes:
        logging.debug(f'Starting integration with ProcessPoolExecutor and {n_jobs} workers')
        with concurrent.futures.ProcessPoolExecutor(max_workers=n_jobs) as executor:
            result = integrate(math.cos, 0, math.pi / 2, 100000, n_jobs)
    else:
        logging.debug(f'Starting integration with ThreadPoolExecutor and {n_jobs} workers')
        result = integrate(math.cos, 0, math.pi / 2, 100000, n_jobs)

    end_time = time.time()
    logging.debug(f'Integration completed in {end_time - start_time} seconds with {n_jobs} workers')
    return end_time - start_time

def compare_execution_times():
    cpu_num = os.cpu_count()
    times_thread = []
    times_process = []

    for n_jobs in range(1, cpu_num * 2 + 1):
        time_thread = run_integration(n_jobs, use_processes=False)
        times_thread.append(time_thread)

        time_process = run_integration(n_jobs, use_processes=True)
        times_process.append(time_process)

    with open('integrate_execution_times.txt', 'w') as f:
        f.write('Number of Workers,ThreadPoolExecutor Time,ProcessPoolExecutor Time\n')
        for i, (t_thread, t_process) in enumerate(zip(times_thread, times_process), start=1):
            f.write(f'{i},{t_thread},{t_process}\n')

if __name__ == '__main__':
    compare_execution_times()