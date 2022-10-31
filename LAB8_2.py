class Node:

    def __init__ (self, data):
        self.data = data
        self.right = None
        self.left = None
        self.height = 1

class AVL_Tree:

    #  def __init__ (self, node, item):
    #     self.right = None
    #     self.left = None

    def insert(self, root, data):
     
        # Step 1 - Perform normal BST
        if not root:
            return Node(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        root.height = 1 + max(self.getHeight(root.left),
                           self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and data < root.left.data:
            return self.rightRotate(root)
 
        if balance < -1 and data > root.right.data:
            return self.leftRotate(root)

        if balance > 1 and data > root.left.data:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and data < root.right.data:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
 
        return root

    def leftRotate(self, z):
 
        y = z.right
        T2 = y.left
 
        # Perform rotation
        y.left = z
        z.right = T2
 
        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                         self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                         self.getHeight(y.right))
 
        # Return the new root
        return y
 
    def rightRotate(self, z):
 
        y = z.left
        T3 = y.right
 
        # Perform rotation
        y.right = z
        z.left = T3
 
        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                        self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                        self.getHeight(y.right))
 
        # Return the new root
        return y
 
    def getHeight(self, root):
        if not root:
            return 0
 
        return root.height
 
    def getBalance(self, root):
        if not root:
            return 0
 
        return self.getHeight(root.left) - self.getHeight(root.right)
 
    def preOrder(self, root):
 
        if not root:
            return
 
        print("{0} ".format(root.data), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

def printTree( root, level = 0):
    if root != None:
        printTree(root.right, level + 1)
        print('     ' * level, root.data)
        printTree(root.left, level + 1)

T = AVL_Tree()
root = None
inp = input("Enter Input : ").split(" ")
a = inp[-1].split("/")
inp[-1] = a[0]
n = a[1]

for i in inp :

    if i == "/":
        break
    root = T.insert(i)
    printTree(root)
    print("--------------------------------------------------")

T.preOrder(root)