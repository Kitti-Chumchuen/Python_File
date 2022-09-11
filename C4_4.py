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
    
    def get(self,i):
        return self.items[i]

#--------------------- Program ------------------#
pair = input('Enter Input : ')
mq = Queue()
yq = Queue()
mw = Queue()
yw = Queue()
m = []
y = []

act = ["Eat","Game","Learn","Movie"]
plc = ["Res.","ClassR.","SuperM.","Home"]
pair = pair.split(',')

for i in pair:
    n = i.split(' ')
    mq.enQueue(n[0])
    yq.enQueue(n[1])

for i in pair:
    m.append(mq.deQueue())
    y.append(yq.deQueue())

countR = 0
c = 0
print('My   Queue = ',end=(''))
for i in pair:
    c+=1
    print(m[countR],end=(''))
    if c<len(pair):
        print(', ',end=(''))
    countR+=1
print('')

countR = 0
c = 0
print('Your Queue = ',end=(''))
for i in pair:    
    c+=1
    print(y[countR],end=(''))
    if c<len(pair):
        print(', ',end=(''))
    countR+=1
print('')

for i in m:
    n = i.split(':')
    mw.enQueue(n[0])
    mw.enQueue(n[1])
for i in y:
    n = i.split(':')
    yw.enQueue(n[0])
    yw.enQueue(n[1])

countA = 0
countP = 1
countR = 0
print('My   Activity:Location = ',end=(''))
for i in m:
    countR+=1
    print(act[int(mw.get(countA))]+':'+plc[int(mw.get(countP))],end=(''))
    if countR < len(m):
        print(', ',end=(''))
    else:
        print('')
    countA+=2
    countP+=2

countA = 0
countP = 1
countR = 0
print('Your Activity:Location = ',end=(''))
for i in y:
    countR+=1
    print(act[int(yw.get(countA))]+':'+plc[int(yw.get(countP))],end=(''))
    if countR < len(y):
        print(', ',end=(''))
    else:
        print('')
    countA+=2
    countP+=2

countR = 0
point = 0
countT = 0
c = 0
for i in m:
    a  = mw.get(countR  )
    a1 = mw.get(countR+1)
    b  = yw.get(countR  )
    b1 = yw.get(countR+1)
    if a==b and a1==b1:
        point+=4
    elif a==b:
        point+=1
    elif a1==b1:
        point+=2
    else:
        point-=5
    if countT<len(m):
        countR+=2
    countT+=1

if point>=7:
    print("Yes! You're my love! : Score is",point,end=('.'))
elif point<7 and point>0:
    print("Umm.. It's complicated relationship! : Score is",point,end=('.'))
else:
    print("No! We're just friends. : Score is",point,end=('.'))