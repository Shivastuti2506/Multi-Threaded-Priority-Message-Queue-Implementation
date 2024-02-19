import threading
import queue

class ThreadPool:
    def __init__(self, num_threads):
        self.pool = []
        self.lock = threading.Lock()
        self.tasks = queue.Queue()  # Define the tasks queue
        for _ in range(num_threads):
            thread = threading.Thread(target=self.worker)
            thread.daemon = True
            thread.start()
            self.pool.append(thread)

    def worker(self):
        while True:
            task, args = self.tasks.get()  # Retrieve task and args from the tasks queue
            task(*args)
            self.tasks.task_done()

    def execute(self, task, *args):
        self.tasks.put((task, args))  # Put task and args into the tasks queue
