class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        nn = Node(item)
        if(self.head):
            cur = self.head
            while(cur.next):
                cur = cur.next
            cur.next = nn
        else:
            self.head = nn

    def addHead(self, item):
        nn = Node(item)
        nn.next = self.head
        self.head = nn

    def search(self, item):
        if not self.isEmpty():
            cur, s = self.head, str(self.head.value)
            while cur != None:
                s = str(cur.value)
                if s == str(item):
                    return "Found "+ item +" in "+self.__str__()
                cur = cur.next
        if self.isEmpty():
            return "Not Found "+item+" in Empty"
        else:
            return "Not Found "+item+" in "+self.__str__()

    def index(self, item):
        if not self.isEmpty():
            ind, cur, s = 0, self.head, str(self.head.value)
            while (cur):
                s = str(cur.value)
                if s == str(item):
                    return ind
                cur = cur.next
                ind += 1
        return -1

    def size(self):
        s, cur = 0, self.head
        while (cur):
            cur = cur.next
            s += 1 
        return s

    def pop(self, pos):
        cur, ind = self.head, 0
        if pos>=0 or pos<self.size():
            if not self.isEmpty():
                if ind == pos:
                    self.head = self.head.next
                    #return "Success"
                while (cur):
                    if ind == pos-1:
                        cur.next = cur.next.next
                        #return "Success"
                    cur = cur.next
                    ind += 1
        #return "Out of Range"
    
    def addBY(self, index, data):
        nn = Node(data)
        cur = self.head
        if index == 0:
          self.addHead(data)
        else:
          for i in range(0,self.size()):
            if i == index-1:
              nn.next = cur.next
              cur.next = nn
            cur = cur.next

# ---------------------- Program ---------------------- #
            
L = LinkedList()
inp = input("Enter Input : ").split(",")

L.append("|")
for i in inp:
    ind = L.index("|")
    if i[:1] == "I":
        ex = i.split(" ")
        L.addBY(ind,ex[1])
    if i[:1] == "L":
        if ind>0:
            L.pop(ind)
            L.addBY(ind-1,"|")
    if i[:1] == "R":
        if ind+1<L.size():
            L.pop(ind)
            L.addBY(ind+1,"|")
    if i[:1] == "B":
        if ind-1>=0:
            L.pop(ind-1)
    if i[:1] == "D":
        if ind+1<L.size():
            L.pop(ind+1)

print(L.__str__())