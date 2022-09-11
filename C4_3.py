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

#--------------------- Program ------------------#
code=input('Enter code,hint : ')
ch=Queue()
count=0
pattern=ord(code[-1])-ord(code[0])
for i in code:
    if count<len(code)-2:
        ch.enQueue(chr((ord(i)+pattern)))
        print(ch.items)
    count+=1