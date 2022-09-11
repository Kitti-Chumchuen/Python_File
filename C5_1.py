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

    def get(self):
        if self.isEmpty():
            return "Empty"
        cur = self.head
        print(str(self.head.value),end=(''))
        while cur.next != None:
            print(str(cur.next.value),end=(''))
            cur = cur.next
            
# ------------------- Program ------------------- #
L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1}".format(L.search(i[3:]), (' ')))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)