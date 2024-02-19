from priority_message_queue import PriorityMessageQueue
from thread_pool import ThreadPool
from msg_sender import MessageSender
from thread_with_priority import ThreadWithPriority
import time

def main():
    # Testing for PriorityMessageQueue
    test_priority_message_queue()

    # Testing for message passing system
    test_message_passing()

def test_priority_message_queue():
    print("Testing PriorityMessageQueue:")
    message_queue = PriorityMessageQueue()

    # Enqueue messages with priorities
    message_queue.enqueue_message("Message 1", priority=1)
    message_queue.enqueue_message("Message 2", priority=3)
    message_queue.enqueue_message("Message 3", priority=2)

    # Peek at the highest priority message 
    peeked_message = message_queue.peek_message()
    print("Peeked message:", peeked_message)

    # Dequeue messages until the queue is empty
    print("Dequeuing messages:")
    while not message_queue.is_empty():
        dequeued_message = message_queue.dequeue_message()
        print("Dequeued message:", dequeued_message)

def test_message_passing():
    print("\nTesting Message Passing:")
    message_queue = PriorityMessageQueue()
    thread_pool = ThreadPool(num_threads=3)
    message_sender = MessageSender(message_queue)

    # Creating threads
    threads = []
    for i in range(5):  # Creating 5 threads
        thread = ThreadWithPriority(thread_id=i, message_queue=message_queue, thread_pool=thread_pool)
        thread.start()
        threads.append(thread)

    # Sending messages with varying priorities
    message_sender.send_message(recipient_thread_id=1, message="first priority message", priority=1)
    message_sender.send_message(recipient_thread_id=2, message="third priority message", priority=3)
    message_sender.send_message(recipient_thread_id=3, message="second priority message", priority=2)

    # Wait for threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()

