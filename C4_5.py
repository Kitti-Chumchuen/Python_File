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
    
    def get(self,i):
        return self.items[i]

    def ins(self,y,ch):
        self.items.insert(y,ch) 

#--------------------- Program ------------------#
a = input ('Enter Input (Normal, Mirror) : ')
a = a.split(' ')

n = Queue() #Normal Queue
m = Queue() #Mirror Queue
nbomb = []
mbomb = []
nexp = 0
mexp = 0
countW = 0
inrCount = 0
y = 0
t = 0
f = 0


for i in a[1]:
    m.ins(0,i)
for i in a[0]:
    n.enQueue(i)
a = m.size()
b = n.size()


while countW < 5: #len(a[0]+a[1])

    count = 0    
    for x in range(0,a):
        if count+2<m.size() and m.get(count+2)!=None:
            if m.get(count)==m.get(count+1) and m.get(count)==m.get(count+2):
                mbomb.append(m.get(count))
                m.deQueue(count)
                m.deQueue(count)
                m.deQueue(count)
                mexp+=1
                count=0
                t=1
        else:
            break
        if t==0:
            count+=1
        else:
            count=0
            t=0

    count = 0    
    for x in range(0,a):
        if count+2<m.size() and m.get(count+2)!=None:
            if m.get(count)==m.get(count+1) and m.get(count)==m.get(count+2):
                mbomb.append(m.get(count))
                m.deQueue(count)
                m.deQueue(count)
                m.deQueue(count)
                mexp+=1
                count=0
        else:
            break
        count+=1

    count = 0
    for x in range(0,b):
        if count+2<n.size() and n.get(count+2)!=None:
            if n.get(count)==n.get(count+1) and n.get(count)==n.get(count+2):
                if mbomb!=[]:
                    if mbomb[0] == n.get(count):
                        inrCount+=1
                    n.ins(count+2,mbomb.pop(0))
                    count+=3
                else:
                    nbomb.append(n.get(count))
                    count+=2
        else:
            break
        count+=1

    count = 0
    for x in range(0,b):
        if count+2<n.size() and n.get(count+2)!=None:
            if n.get(count)==n.get(count+1) and n.get(count)==n.get(count+2):             
                n.deQueue(count)
                n.deQueue(count)
                n.deQueue(count)
                nexp+=1
                count=0
        else:
            break
        count+=1

    nbomb = []
    mbomb = []
    countW+=1


normal = []
exp = []

print('NORMAL :')
print(n.size())

if not n.isEmpty():
    count = 0
    for x in range(0,n.size()):
        normal.insert(0,n.get(count))
        count+=1

    count = 0
    for x in range(0,n.size()):
        print(normal[count],end=(''))
        count+=1
    print('')
else:
    print('Empty')
if inrCount!=0:
    nexp=nexp-inrCount
print(nexp,'Explosive(s) ! ! ! (NORMAL)')

if inrCount!=0:
    print('Failed Interrupted',inrCount,'Bomb(s)')
print('------------MIRROR------------')
print(': RORRIM')
print(m.size())


if not m.isEmpty():
    count = 0
    for x in range(0,m.size()):
        exp.insert(0,m.get(count))
        count+=1

    count = 0
    for x in range(0,m.size()):
        print(exp[count],end=(''))
        count+=1
    print('')
else:
    print('ytpmE')

print('(RORRIM) ! ! ! (s)evisolpxE',mexp)
#print(nbomb,mbomb)