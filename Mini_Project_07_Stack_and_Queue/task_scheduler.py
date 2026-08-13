from collections import deque  # Import deque for creating an efficient queue

class Queue:
    def __init__(self):
        # Initialize the queue as an empty deque
        self.queue = deque()

    def is_empty(self):
        # Return True if the queue has no elements, else False
        return len(self.queue) == 0

    def enqueue(self, task):
        # Add a task at the back of the queue
        self.queue.append(task)
        print(f"Task Added: {task}")  # Print confirmation message after adding the task

    def dequeue(self):
        # Remove and return the task from the front of the queue
        if self.is_empty():  # Check if the queue is empty before attempting dequeue
            return "No tasks to process"  # Return message for empty queue
        return self.queue.popleft()  # Remove and return the first element in O(1)

    def peek(self):
        # Return the task at the front of the queue without removing it
        if self.is_empty():  # Check if the queue is empty before peeking
            return "No tasks available"  # Return message for empty queue
        return self.queue[0]  # Access the first element without removal

# Driver Code
scheduler = Queue()  # Instantiate a Queue to act as a task scheduler

# Add tasks to the scheduler
scheduler.enqueue("Email Client")        # Add "Email Client" task
scheduler.enqueue("Backup Database")    # Add "Backup Database" task
scheduler.enqueue("Generate Report")    # Add "Generate Report" task

# Peek at the next task in the scheduler
print("\nNext Task:", scheduler.peek())  # Display the task at the front of the queue without removal

# Process the first task by removing it from the queue
print("Processing:", scheduler.dequeue())  # Remove and display the task being processed

# Peek at the next task to check the updated front of the queue
print("Next Task:", scheduler.peek())  # Display the updated front task after one task is processed

# Process all remaining tasks in the queue
while not scheduler.is_empty():  # Loop until the queue is empty
    print("Processing:", scheduler.dequeue())  # Remove and display each task being processed

# Display a message indicating all tasks have been completed
print("All Tasks Completed.")  # Notify that all tasks in the queue are processed and completed