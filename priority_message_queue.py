import heapq
import threading

class PriorityMessageQueue:
    def __init__(self):
        self.queue = []
        self.lock = threading.Lock()

    def enqueue_message(self, message, priority):
        with self.lock:
            heapq.heappush(self.queue, (-priority, message))

    def dequeue_message(self):
        with self.lock:
            if not self.queue:
                return None
            return heapq.heappop(self.queue)[1]  # Return the message part only

    def peek_message(self):
        with self.lock:
            if not self.queue:
                return None
            return self.queue[0][1]  # Return the message part only

    def is_empty(self):
        with self.lock:
            return len(self.queue) == 0


