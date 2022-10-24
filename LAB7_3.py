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
    
    def is_more_than_k(self, node, k):
        if node != None:
            self.is_more_than_k(node.right, k)
            if int(node.data) > int(k):
                n = int(node.data)
                n = n * 3
                node.data = n
            self.is_more_than_k(node.left, k)

        return node


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
root = T.is_more_than_k(root, k)
T.printTree(root)