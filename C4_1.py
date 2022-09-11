class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def enQueue(self, item):
        self.items.append(item)

    def deQueue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


a = input('Enter Input : ')
a_st = a.split(',')
count = 0
for x in a_st:
    if 'E' in x:
        n = x.split(' ')
        a_st[count] = n[1]
    count+=1
data = Queue()
ref = []
count = 0
r = 0
for i in a_st:
    r+=1
    if i == 'D':
        if data.isEmpty():
            print('-1')
            if r == len(a_st):
                print('Empty')     
        else:
            print('Pop ',end=(''))
            print(data.deQueue(),end=(''))
            print(' size in queue is',data.size())
            count-=1
    else:
        data.enQueue(i)
        print('Add',i,end=(''))
        print(' index is',count)
        count+=1

    if r == len(a_st) and data.size() != 0:
            print('Number in Queue is :  ',end=(''))
            print(data.items)