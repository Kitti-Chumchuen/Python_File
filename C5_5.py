class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)
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
                a = self.head.value
                self.head = self.head.next
                return a
            while (cur):
                if ind == pos-1:
                    a = cur.next.value
                    cur.next = cur.next.next
                    return a
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

def createLL(LL):
    L = LinkedList()
    for i in LL:
        L.append(i)
    return L

def printLL(head):
    return head.__str__()

def SIZE(head):
    return head.size()

def scarmble(head, b, r, size):
    UP = LinkedList()
    LO = LinkedList()
    n  = 1
    c  = head.__str__().split(" ")   

    NB = int((b/100)*size)
    NR = int((r/100)*size)
    FB = "{:.3f}".format(b)
    FR = "{:.3f}".format(r)

    for i in range(0,size):
        UP.append(c[i]) 
    for i in range(0,size):
        if i < NB:
            a = UP.pop(0)
            UP.append(a)
    print("BottomUp",FB,"% :",UP.__str__())
    for i in range(0,UP.size()):
        if i >= NR:
            LO.append(UP.pop(NR))
    DLO = LO.size()
    # print("UP",printLL(UP))
    # print("LO",printLL(LO))
    for i in range(0,size):
        if not LO.isEmpty():
            if i <= UP.size():
                UP.addBY(n,LO.pop(0))
            else:
                UP.append(LO.pop(0))
        n += 2
    print("Riffle",FR,"% :",UP.__str__())

    n = 1
    for i in range(0,size):
        if i < DLO:
            UP.append(UP.pop(n))
        n+=1
    print("Deriffle",FR,"% :",UP.__str__())

    for i in range(0,size):
        if i < NB:
            UP.addHead(UP.pop(-1))
    print("Debuttom",FB,"% :",UP.__str__())

# ---------------------- Program ---------------------- #  

inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
h = createLL(inp1.split())
for i in inp2.split('|'):
    print("Start : ",printLL(h))
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":
        scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B":
        scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
    print('-' * 50) 
