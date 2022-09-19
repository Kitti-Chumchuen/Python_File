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
            return " "
        cur, s = self.head, str(self.head.data)
        while cur.next != None:
            cur = cur.next
            s += "->" + str(cur.data)
        return s

    def str_reverse(self):
        if self.isEmpty():
            return " "
        cur, s = self.tail, str(self.tail.data)
        while cur.prev != None:
            cur = cur.prev
            s += "->" + str(cur.data)
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
        tt = Node(data)
        cur = self.head
        tur = self.tail
        ss = self.size()
        i = 0
        # if int(index) == ss-1:
        #     self.append(data)
        if int(index) == 0:
            self.add_before(data)
        else:
            if ss == int(index):
                print("YES")
                while cur:
                    if cur.next == None:
                        nn.next = cur
                        cur = nn
            else:
                while cur:
                    if i == int(index) - 1:
                        nn.next = cur.next
                        cur.next = nn
                    i += 1
                    cur = cur.next

            i = 0
            snr = self.tail
            while snr.prev:
                if ss == int(index):
                    nn.prev = snr
                    snr = nn
                if ss - int(index) == 0:
                    nn.prev = self.tail
                    self.tail.next = nn
                    nn.next = None
                    self.tail = nn
                    break
                elif i == ss-int(index)-1:
                    tt.prev = snr.prev
                    snr.prev = tt
                    break
                i += 1
                snr = snr.prev

    def removeBY(self, item):
        count = 0
        if self.isEmpty():
            # print("Not Found!")
            return -1
        if self.head.next is None:
            if str(self.head.data) == str(item):
                self.head = None
                self.tail = None
            else:
                # print("Not Found!")
                count = -1
            return count

        if str(self.head.data) == str(item):
            self.head = self.head.next
            self.head.prev = None
            return count

        n = self.head
        while n.next is not None:
            if str(n.data) == str(item):
                break
            count += 1
            n = n.next
        if n.next is not None:
            n.prev.next = n.next
            n.next.prev = n.prev
        else:
            if str(n.data) == str(item):
                n.prev.next = None
            else:
                # print("Not Found!")
                count = -1
        return count


# ------------- Program -------------- #
dl = DoublyLinked()
inp = input("Enter Input : ").split(',')

for i in inp:
    a = i.split(' ')
    if a[0] == "":
        a[0] = a[1]
        a[1] = a[2]

    n = 0
    if a[0] == "Ab":
        dl.add_before(a[1])
    elif a[0] == "A":
        dl.append(a[1])
    elif a[0] == "I":
        b = a[1].split(":")
        if dl.isEmpty() and b[0] != "0":
            print("Data cannot be added")
        elif b[0] == "-1" or int(b[0]) < -1:
            print("Data cannot be added")
        elif int(b[0]) > dl.size():
            print("Data cannot be added")
        else:
            print("index =", b[0], "and data =", b[1])
            dl.insert(b[0], b[1])
    elif a[0] == "R":
        if dl.isEmpty():
            print("Not Found!")
        else:
            n = dl.removeBY(a[1])
            if n == -1:
                print("Not Found!")
            else:
                print("removed :", a[1], "from index :", n)
    print("linked list :", dl.__str__())
    print("reverse :", dl.str_reverse())
