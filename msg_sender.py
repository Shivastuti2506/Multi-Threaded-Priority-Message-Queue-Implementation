import threading
from thread_with_priority import ThreadWithPriority

class MessageSender:
    def __init__(self, message_queue):
        self.message_queue = message_queue

    def send_message(self, recipient_thread_id, message, priority):
        # Add message to the message queue with specified priority
        self.message_queue.enqueue_message((recipient_thread_id, message), priority)
        # Wake up the recipient thread if it's waiting for messages
        for thread in threading.enumerate():
            if isinstance(thread, ThreadWithPriority) and thread.thread_id == recipient_thread_id:
                thread.wake_up()
