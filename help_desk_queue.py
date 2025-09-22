
from node import Node

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if not self.front: 
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.front: 
            return None
        dequeued_value = self.front.value
        self.front = self.front.next
        if not self.front: 
            self.rear = None
        return dequeued_value

    def peek(self):
        return None if not self.front else self.front.value

    def print_queue(self):
        if not self.front:
            print("Queue is empty.")
            return
        current = self.front
        while current:
            print(f"- {current.value}")
            current = current.next
    


def run_help_desk():

    queue = Queue()

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            queue.enqueue(name)
            print(f"{name} added to the queue.")

        elif choice == "2":
            customer = queue.dequeue()
            if customer:
                print(f"{customer} has been helped.")
            else:
                print("No customers in queue.")

        elif choice == "3":
            customer = queue.peek()
            if customer:
                print(f"Next customer: {customer}")
            else:
                print("No customers in queue.")

        elif choice == "4":
            print("\nWaiting customers:")
            queue.print_queue()

        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()


#The custom linked list implementation for the waitlist manager is designed to handle dynamic customer management in a flexible and efficient way. The system uses two main classes: Node and LinkedList. Each Node stores a customer’s name along with a reference to the following node in the sequence. The LinkedList class manages the overall structure, starting from the head, which always points to the first customer in the waitlist. 
#The head plays a critical role because it serves as the entry point into the list. All operations—whether adding to the front, adding to the end, removing a customer, or printing the list—begin by referencing the head. When a new customer is added to the front, the new node becomes the head. When a customer is removed, the head may shift if it was the first element being removed. Essentially, the head acts like an anchor that keeps the list accessible and navigable. 
#A real engineer might need a custom linked list like this in scenarios where the number of items changes constantly, and memory needs to be managed efficiently. Such as real-time ticketing or reservation systems, task scheduling, operating system process management, or network packet queues. Unlike arrays, linked lists avoid costly resizing operations and allow for fast insertions and removals, making them valuable in systems where speed and flexibility are critical. 