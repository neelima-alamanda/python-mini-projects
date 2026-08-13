class Queue:
    def __init__(self):
        # Initialize an empty queue using a Python list
        self.queue = []

    def is_empty(self):
        # Check if the queue is empty
        return len(self.queue) == 0

    def enqueue(self, data):
        # Add an element to the end of the queue
        self.queue.append(data)

    def dequeue(self):
        # Remove and return the front element of the queue
        if self.is_empty():  # Check if the queue is empty before dequeueing
            return "Queue is empty"
        
        removed = self.queue.pop(0)  # Remove the element at index 0 (front)
        return removed

    def peek(self):
        # Return the front element of the queue without removing it
        if self.is_empty():  # Check if the queue is empty before peeking
            return "Queue is empty"
        else:
            return self.queue[0]  # Return the first element in the list


# Driver Code: Test the queue functionality

# Initialize an empty queue
queue = Queue()

# Add elements to the queue
queue.enqueue(10)  # Enqueue the number 10
print("10 added to the queue.")
queue.enqueue(20)  # Enqueue the number 20
print("20 added to the queue.")
queue.enqueue(30)  # Enqueue the number 30
print("30 added to the queue.")

# Display the front element of the queue
print("Front Element:", queue.peek())  # Expected: 10

# Remove the front element
print("Dequeued Element:", queue.dequeue())  # Expected: 10

# Display the front element after dequeue
print("Front Element after Dequeue:", queue.peek())  # Expected: 20

# Check whether the queue is empty
print("Is Queue Empty?", queue.is_empty())  # Expected: False