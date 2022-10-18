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
        if self.root != None:
            if data < self.root:
                if self.root.left:
                    nn.left = self.root.left
                    self.root.left.left = nn
                else:
                    self.root.left = nn
            elif data > self.root:
                if self.root.right:
                    nn.right = self.root.right
                    self.root.right.right = nn
                else:
                    self.root.right = nn
        else:
            self.root = data
        print(data)

    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)