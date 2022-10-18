class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        nn = Node(data)
        if self.root == None:
            self.root = nn
        else:
            cur = self.root 
            while cur != None:
                if int(cur.data) > int(data) :
                    if cur.left == None :
                        cur.left = nn
                        break
                    else :
                        cur = cur.left

                if int(cur.data) < int(data) :
                    if cur.right == None :
                        cur.right = nn
                        break
                    else :
                        cur = cur.right

                if int(cur.data) == int(data):
                    if cur.left == None :
                        cur.left = nn
                        break
                    else :
                        cur = cur.left
        return self.root
    
    def time3(self, node, k):
        curR = node
        curL = node 
        if node != None:
            while curL.left != None:
                print(curL.data,"L")
                if int(curL.data) > int(k):
                    n = int(curL.left.data)
                    nn = Node(n*3)
                    curL.left = nn 
                #print(str(curL.data))
                curL = curL.left

            while curR != None:
                print(curR.data,"R")
                if int(curR.data) > int(k):
                    n = int(curR.right.data)
                    nn = Node(n*3)
                    curR.right = nn 
                #print(str(curR.data))
                curR = curR.right 
        return self.root

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level , node)
            self.printTree(node.left, level + 1)

T = BST()
inp = input('Enter Input : ').split(" ")
n, k = 0, 0
for i in inp[-1]:
    if i == "/":
        break
    n += 1
a = inp[-1]
k = int(a[n+1:])
inp[-1] = a[:n]
#print(inp)
for i in inp:
    root = T.insert(i)
T.printTree(root)
print("--------------------------------------------------")
T.time3(root, k)
T.printTree(root)