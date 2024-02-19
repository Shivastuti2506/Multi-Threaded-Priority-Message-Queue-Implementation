import threading
import queue

class PriorityMessageQueue:
    def __init__(self):
        self.lock = threading.Lock()  # Mutex lock for thread safety
        self.messages = queue.PriorityQueue()  # Priority queue to store messages

    def enqueue_message(self, message, priority):
        with self.lock:
            self.messages.put((priority, message))

    def dequeue_message(self):
        with self.lock:
            if not self.messages.empty():
                return self.messages.get()[1]
            else:
                return None

    def peek_message(self):
        with self.lock:
            if not self.messages.empty():
                return self.messages.queue[0][1]
            else:
                return None

    def is_empty(self):
        with self.lock:
            return self.messages.empty()
