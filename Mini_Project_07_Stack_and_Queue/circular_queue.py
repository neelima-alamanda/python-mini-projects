class CircularQueue:
    def __init__(self, capacity):
        # Initialize the circular queue with given capacity
        self.queue = [None] * capacity  # Create a fixed-size list to hold elements
        self.capacity = capacity        # Maximum capacity of the queue
        self.Rear = 0                   # Rear pointer for enqueue operations
        self.Front = 0                  # Front pointer for dequeue operations
        self.size = 0                   # Current size of the queue

    def is_empty(self):
        # Check if the queue is empty
        return self.size == 0

    def is_full(self):
        # Check if the queue is full
        return self.size == self.capacity

    def enqueue(self, data):
        # Add an element to the rear of the queue
        if self.is_full():  # Check if the queue is full before enqueue
            return "Queue is Full"
        else:
            self.queue[self.Rear] = data             # Place the new element at the Rear position
            self.Rear = (self.Rear + 1) % self.capacity  # Move Rear forward circularly
            self.size += 1                           # Increment the size of the queue

    def dequeue(self):
        # Remove and return the front element of the queue
        if self.is_empty():  # Check if the queue is empty before dequeue
            return "Queue is empty"
        else:
            removed = self.queue[self.Front]         # Retrieve the Front element
            self.queue[self.Front] = None           # Nullify the Front position after removal
            self.Front = (self.Front + 1) % self.capacity  # Move Front forward circularly
            self.size -= 1                          # Decrease the size of the queue
            return removed

    def peek(self):
        # Return the front element without removing it
        if self.is_empty():  # Check if the queue is empty before peeking
            return "Queue is empty"
        else:
            return self.queue[self.Front]           # Return the Front element

# Driver Code
queue = CircularQueue(5)  # Create a circular queue with capacity 5

# Add elements to the queue
queue.enqueue(10)  # Enqueue 10
queue.enqueue(20)  # Enqueue 20
queue.enqueue(30)  # Enqueue 30

# Display the front element
print("Front Element:", queue.peek())  # Expected: 10

# Remove the front element
print("Dequeued Element:", queue.dequeue())  # Expected: 10

# Display the front element after dequeue
print("Front Element after Dequeue:", queue.peek())  # Expected: 20

# Check whether the queue is empty
print("Is Queue Empty?", queue.is_empty())  # Expected: False

# Check whether the queue is full
print("Is Queue Full?", queue.is_full())  # Expected: False