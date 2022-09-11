class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
 
 
class Stack:
 
    def __init__(self):
        self.head = Node("head")
        self.size = 0
 
    # def __str__(self):
    #    if self.isEmpty():
    #        return "Empty"
    #    cur, s = self.head, str(self.head) + " "
    #    while cur:
    #        s += str(cur.value) + " "
    #        cur = cur.next
    #    return s
    # String representation of the stack
    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head.next, ""
        while cur:
            s += str(cur.value) + " "
            cur = cur.next
        return s
 
    # Get the current size of the stack
    def getSize(self):
        return self.size
 
    # Check if the stack is empty
    def isEmpty(self):
        return self.size == 0
 
    # Get the top item of the stack
    def peek(self):
 
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value
 
    # Push a value into the stack.
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
 
    # Remove a value from the stack and return.
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value

# ------------------- Program ------------------- #
a = Stack()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:1] == "A":
        a.push(i[1:])
        print("Add =",i[1:],"and Size =", a.getSize())
    elif i[:1] == "P":
        if not a.isEmpty():
            print("Pop =",a.pop(),"and Index =", a.getSize())
        else:
            print("-1")

print("Value in Stack =",a.__str__())  