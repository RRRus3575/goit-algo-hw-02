import queue
import random
import time
import threading
import keyboard

request_queue = queue.Queue()

request_id = 1

def generate_request():
    global request_id
    request = f"Request {request_id}"
    request_id += 1
    request_queue.put(request)
    print(f"Generated: {request}")

def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Processing: {request}")
        time.sleep(random.uniform(0.1, 1.0))  
        print(f"Completed: {request}")
    else:
        print("Queue is empty")

def main_loop(stop_event):
    while not stop_event.is_set():
        generate_request()
        time.sleep(random.uniform(0.1, 0.5))  
        process_request()

def main():
    stop_event = threading.Event()
    main_thread = threading.Thread(target=main_loop, args=(stop_event,))
    main_thread.start()

    print("Press any key to terminate the program.")
    
    keyboard.on_press(lambda event: stop_event.set())
    
    main_thread.join()
    
    print("Program terminated by user")


if __name__ == "__main__":
    main()
