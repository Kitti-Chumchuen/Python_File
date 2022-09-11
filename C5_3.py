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
        if not self.isEmpty():
            if ind == pos:
                self.head = self.head.next
                return "Success"
            while (cur):
                if ind == pos-1:
                    cur.next = cur.next.next
                    return "Success"
                cur = cur.next
                ind += 1
        return "Out of Range"

# ---------------------- Program ---------------------- #

L1 = LinkedList()
L2 = LinkedList()
inp = input("Enter Input (L1,L2) : ").split(" ")
L1 = inp[0].split("->")
L2 = inp[1].split("->")


print("L1    : ", end=(""))
for i in L1:
    print(i, end=(" "))
print("")


print("L2    : ", end=(""))
for i in L2:
    print(i, end=(" "))
print("")


for l in range(0,len(L2)):
    if len(L2)>1:
        L1.append(L2.pop(-1))
    else:
        L1.append(L2.pop(0))


print("Merge : ", end=(""))
for i in L1:
    print(i,end=(" "))
print("")