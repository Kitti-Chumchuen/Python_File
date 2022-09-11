# Create the Node class
class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None

# Create the doubly linked list

class doubly_linked_list:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head)
        for i in range(0, self.size()):
            s += "->"+str(cur.next)
            cur = cur.next
        return s

    def str_reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail)
        for i in range(0, self.size()):
            s += "->"+str(cur.prev)
            cur = cur.prev
        return s
# Define the push method to add elements
    def addBefore(self, data):
        nn = Node(data)
        nn.next = self.head
        if not self.isEmpty():
            self.head.prev = nn
        self.head = nn

    def isEmpty(self):
        return self.head == None

    def size(self):
        s, cur = 0, self.head
        while cur:
            cur = cur.next
            s += 1
        return s
# Define the insert method to insert the element		
    def insert(self, index, data):
        nn = Node(data)
        nn.next = self.head
        if self.isEmpty() and index!=0:
            self.head.next = nn
        else:
            cur = self.head
            for i in range(0, self.size()):
                if i == index:
                    cur.next = nn
                    break

    def listprint(self, node):
      for i in range(0, self.size()):
         print(node.data),
         last = node
         node = node.next

    # def listprint(self):
    #    cur = self.head
    #  while cur is None:
    #     print(node.data)
    #     last = node
    #     node = node.next

# Define the method to print the linked list 
    # def listprint(self):
    #    cur = self.head
    #    for i in range(0, self.size()):
    #        print(cur,end=(" "))
    #        cur = cur.next

dllist = doubly_linked_list()
dllist.addBefore(12)
dllist.addBefore(8)
dllist.addBefore(62)
dllist.insert(2, 13)
dllist.listprint(dllist.head)
#print(dllist.__str__())