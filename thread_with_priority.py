import threading
import time

class ThreadWithPriority(threading.Thread):
    def __init__(self, thread_id, message_queue, thread_pool):
        super().__init__()
        self.thread_id = thread_id
        self.message_queue = message_queue
        self.thread_pool = thread_pool
        self.sleeping = False
        self.wake_event = threading.Event()

    def run(self):
        while True:
            message = self.message_queue.dequeue_message()
            if message:
                print(f"Thread {self.thread_id} received message: {message}")
                # Perform a simple action using the thread pool
                self.thread_pool.execute(self.simple_action, message)
            else:
                self.sleeping = True
                self.wake_event.clear()  # Clear wake event
                self.wake_event.wait()   # Sleep until wake event is set
                self.sleeping = False

    def wake_up(self):
        if self.sleeping:
            self.wake_event.set()  # Set wake event

    def simple_action(self, message):
        # Simulating a simple action (printing the message)
        print(f"Thread {self.thread_id} performing action: {message}")
        time.sleep(1)  # Simulating some processing time
