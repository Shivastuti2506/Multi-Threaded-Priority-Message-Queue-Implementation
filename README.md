# Multi-threaded Priority Message Queue System

## Overview
This project implements a multi-threaded priority message queue system in Python. It allows multiple threads to send messages to each other with varying priorities. Upon receiving a message, the receiving thread performs a simple action using a thread pool for concurrent execution.

## Workflow
1. **Initialization**:
   - Initialize the priority message queue, thread pool, and message sender.

2. **Thread Creation**:
   - Create multiple threads, each with a unique identifier, access to the message queue, and thread pool.

3. **Message Enqueuing**:
   - Threads enqueue messages with priorities into the message queue.

4. **Thread Activation**:
   - Activate threads waiting for messages upon enqueuing, ready to process incoming messages.

5. **Message Processing**:
   - Threads retrieve messages from the queue and execute associated actions concurrently using the thread pool.

6. **Thread Deactivation**:
   - Threads return to a waiting state if the queue becomes empty, awaiting new messages.

7. **Continued Operation**:
   - Threads continue to send, receive, and process messages until completion.

8. **Program Termination**:
   - The program concludes once all threads have finished their tasks and terminated, releasing resources and exiting gracefully.

## Usage by cloning the repository
1. Clone the repository to your local machine.
2. Ensure you have Python 3.6 or higher installed.
3. Run the `main.py` file:
   ```bash
   python main.py

## Usage without cloning the repository
1. you just need to type vscode.dev in the above url .
    ```bash
    https://vscode.dev/github.com/Shivastuti2506/Multi-Threaded-Priority-Message-Queue-Implementation/edit/main/README.md
2. After that, it just asks for some permission for vs code to open, allow the permissions.
3. open the vscode local terminal.
4. Run the `main.py` file:
   ```bash
   python main.py
   

