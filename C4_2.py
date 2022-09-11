class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def enQueue(self, item):
        self.items.append(item)

    def deQueue(self,i):
        return self.items.pop(i)

    def size(self):
        return len(self.items)

#--------------------- Program ------------------#
word=input('Enter people : ')
maR=Queue()
c1R=Queue()
c2R=Queue()
count=0
count1=0
count2=0

for i in word:
    maR.enQueue(i)

for i in word:
    count+=1
    print(count,end=(' '))
    if c1R.size()<=5:
        c1R.enQueue(maR.deQueue(0))
    else:
        c2R.enQueue(maR.deQueue(0))
    if count1==3:
        c1R.deQueue(0)
        count1=0
    if count2==2:
        c2R.deQueue(0)
        count2=0
    if c1R.size()>5:
        c2R.enQueue(c1R.deQueue(c1R.size()-1))
    if not c1R.isEmpty():
        count1+=1
    if not c2R.isEmpty():
        count2+=1

    print(maR.items,c1R.items,c2R.items,end=('\n'))