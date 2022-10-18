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

    # def insert(self, data):
    #     nn = Node(data)
    #     cur = self.root 

    #     if cur == None:
    #         cur = data

    #     #if cur:
    #     while cur != None:
    #         if int(cur.data) > int(data) :
    #             if cur.left == None :
    #                 cur.left = nn
    #             else :
    #                 cur = cur.left

    #         if int(cur.data) < int(data) :
    #             if cur.right == None :
    #                 cur.right = nn
    #             else :
    #                 cur = cur.right
        # else:
        #     cur = nn
        # return self.root

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

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root,0)