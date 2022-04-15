# stack implementation using linklist
class node:
    def __init__(self, data, next):#constructor to define object of node class
        self.data = data
        self.next = next

def push(head, data):
    new_node = node(data, head)
    head = new_node
    return head

def pop(head):
    if head is None:
        return None
    data = head.data
    print()
    print(data,'is poppped')
    head = head.next
    return data, head

def traverse(head):
    while head is not None:
        print(head.data)
        head = head.next

head = node(20, None) # Create a node with data 1
print(head.data,'is pushed')
head = push(head, 30) # Push 2 onto the stack
print(head.data,'is pushed')
head = push(head, 40) # Push 3 onto the stack
print(head.data,'is pushed')
head = push(head, 50) # Push 4 onto the stack
print(head.data,'is pushed')

data, head = pop(head) # Pop the stack
print('\nprint stack using traverse method')
traverse(head) # Print the stack