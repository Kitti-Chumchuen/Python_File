class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinked:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.data)
        while cur.next != None:
            cur = cur.next
            s += "->"+str(cur.data)
        return s

    def str_reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.data)
        while cur.prev != None:
            cur = cur.prev
            s += "->"+str(cur.data)
        return s

    def isEmpty(self):
        return self.head == None

    def size(self):
        s, cur = 0, self.head
        while cur:
            cur = cur.next
            s += 1
        return s

    def append(self, data):
        nn = Node(data)
        nn.prev = self.tail
        if self.isEmpty():
            self.head = nn
            self.tail = nn
            nn.next = None
        else:
            self.tail.next = nn
            nn.next = None
            self.tail = nn

    def add_before(self, data):
        nn = Node(data) 
        nn.next = self.head
        if self.isEmpty():
            self.head = nn
            self.tail = nn
            nn.prev = None
        else:
            self.head.prev = nn
            self.head = nn
            nn.prev = None

    def insert(self, index, data):
        nn = Node(data)
        cur = self.head
        i = 0
        if int(index) == 0:
          self.add_before(data)
        else:
        #   for i in range(0,self.size()):
            while cur:
                if i == int(index)-1:
                    nn.next = cur.next
                    cur.next = nn
                #   nn.prev = None
                #   nn.prev = cur.prev
                #   cur.prev = nn
                if i == int(index)+1:
                    nn.prev = cur.prev
                    cur.prev = nn
                i += 1
                cur = cur.next

    def insert_before(self, temp_node, data): # Inserting a new node before a given node
        nn = Node(data)
        if not self.isEmpty():
            if temp_node != None:
                nn.prev = temp_node.prev
                temp_node.prev = nn
                nn.next = temp_node
                if nn.prev != None:
                    nn.prev.next = nn
                if temp_node == self.head: 
                    self.head = nn

    def remove(self, data):
        nn = Node(data)
        remove = self.data
        self.data = self.data.next
        return remove.data


# ------------- Program -------------- #
dl = DoublyLinked()
inp = input("Enter input : ").split(',')

for i in inp:
    n = 0
    if i[:2] == "Ab":
        dl.add_before(i[3:])
    elif i[:1] == "A":
        dl.append(i[2:])
    elif i[:1] == "I":
        a = i[2:].split(":")
        dl.insert(a[0],a[1]) 
        if dl.isEmpty() and a[0]!=0:
            print("Data cannot be added")
        else:
            print("index =", a[0],"and data =", a[1])
    elif i[:1] == "R":
        if dl.isEmpty() and a[0]!=0:
            print("Not Found!")
        else:
            print("removed :",i[1:],"from index :")
    print("Linked List :", dl.__str__())
    #print(str(dl.head))
    print("reverse :", dl.str_reverse())

#A 3,A 4,Ab 0,I 1:2