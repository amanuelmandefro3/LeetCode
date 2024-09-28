class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.lim = 0
        self.head = None
        self.tail = None

    # Insert at the front
    def insertFront(self, value: int) -> bool:
        if self.lim == self.k:
            return False  # Deque is full 
        newnode = Node(value)
        if self.head:
            newnode.next = self.head
            self.head = newnode
            self.tail.next = self.head  # Circular link 
        else:
            self.head = self.tail = newnode
            self.tail.next = self.head  # Circular link 
        self.lim += 1  # Increment size 
        return True  # Insert successful 

    #  Insert at the rear
    def insertLast(self, value: int) -> bool:
        if self.lim == self.k:
            return False  # Deque is full 
        newnode = Node(value)
        if self.head:
            self.tail.next = newnode
            self.tail = newnode
            self.tail.next = self.head  # Circular link 
        else:
            self.head = self.tail = newnode
            self.tail.next = self.head  # Circular link 
        self.lim += 1  # Increment size 
        return True  # Insert successful 

    #  Delete from the front
    def deleteFront(self) -> bool:
        if not self.head:
            return False  # Deque is empty 
        if self.head == self.tail:
            self.head = self.tail = None  # Only one element 
        else:
            self.head = self.head.next
            self.tail.next = self.head  # Circular link 
        self.lim -= 1  # Decrement size 
        return True  # Deletion successful 

    #  Delete from the rear
    def deleteLast(self) -> bool:
        if not self.head:
            return False  # Deque is empty 
        if self.head == self.tail:
            self.head = self.tail = None  # Only one element 
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            self.tail = current
            self.tail.next = self.head  # Circular link 
        self.lim -= 1  # Decrement size 
        return True  # Deletion successful 

    #  Get the front element
    def getFront(self) -> int:
        if not self.head:
            return -1  # Deque is empty 
        return self.head.val  # Return front element

    # Get the rear element
    def getRear(self) -> int:
        if not self.tail:
            return -1  # Deque is empty 
        return self.tail.val  # Return rear element

    #  Check if deque is empty
    def isEmpty(self) -> bool:
        return self.head is None  # True if empty 

    # Check if deque is full
    def isFull(self) -> bool:
        return self.lim == self.k  # True if full 