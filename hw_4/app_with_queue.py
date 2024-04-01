import os
import time
import threading
import multiprocessing
import logging

logging.basicConfig(filename='queue_pipe_interaction.txt', level=logging.DEBUG, format='%(asctime)s - %(message)s')

def process_a(input_queue, output_queue):
    while True:
        message = input_queue.get()
        if message == 'STOP':
            break
        logging.debug(f'Process A: Received message: {message}')
        output_queue.put(message.lower())

def process_b(input_queue, output_pipe):
    while True:
        message = input_queue.get()
        if message == 'stop':
            break
        logging.debug(f'Process B: Received message: {message}')
        time.sleep(5)
        encoded_message = rot13(message)
        logging.debug(f'Process B: Encoded message: {encoded_message}')
        output_pipe.send(encoded_message)

def rot13(message):
    return ''.join(
        chr((ord(c) - ord('a') + 13) % 26 + ord('a')) if c.islower() else chr((ord(c) - ord('A') + 13) % 26 + ord('A')) if c.isupper() else c
        for c in message
    )


def main():
    input_queue = multiprocessing.Queue()
    output_queue = multiprocessing.Queue()
    parent_conn, child_conn = multiprocessing.Pipe()

    a_process = multiprocessing.Process(target=process_a, args=(input_queue, output_queue))
    b_process = multiprocessing.Process(target=process_b, args=(output_queue, child_conn))

    a_process.start()
    b_process.start()

    def send_messages():
        messages = ['Hello', 'World', 'Multiprocessing', 'Queue', 'Rot13', 'I Love ADVanCed PythOn', 'ITMO, HSE, SPBSU']
        for message in messages:
            logging.debug(f'Main Process: Sending message: {message}')
            input_queue.put(message)
            time.sleep(5)
        input_queue.put('STOP')

    def receive_messages():
        while True:
            message = parent_conn.recv()
            if message is None:
                break
            logging.debug(f'Main Process: Received encoded message: {message}')

    thread_send = threading.Thread(target=send_messages)
    thread_receive = threading.Thread(target=receive_messages)

    thread_send.start()
    thread_receive.start()

    thread_send.join()
    thread_receive.join()

    child_conn.send(None)
    a_process.join()
    b_process.join()

if __name__ == '__main__':
    main()
