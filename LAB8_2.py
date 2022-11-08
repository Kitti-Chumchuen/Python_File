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
        if self.root == None:
            nn = Node(data)
            self.root = nn
        else:
            cur = self.root
            while cur:
                if data > cur.data:
                    if cur.right == None:
                        nn = Node(data)
                        cur.right = nn
                        break
                    else:
                        cur = cur.right
                else:
                    if cur.left == None:
                        nn = Node(data)
                        cur.left = nn
                        break
                    else:
                        cur = cur.left
        return self.root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def closest_value(self, root, value):
        a = int(root.data)
        if value == a:
            return a
        else:
            kid = root.left if value < a else root.right
            if not kid:
                return a
            b = self.closest_value(kid, value)
            return min((a,b), key=lambda x: abs(value-x))

T = BST()
inp = input('Enter Input : ').split(" ")
a = inp[-1].split("/")
inp[-1] = a[0]
n = int(a[1])

for i in inp:
    root = T.insert(int(i))
    T.printTree(root,0)
    print("--------------------------------------------------")

result = T.closest_value(root, n)
print("Closest value of",n,":", result)