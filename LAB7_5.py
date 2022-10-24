class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = None if left == None else left
        self.right = None if right == None else right

    def __str__(self):
        return str(self.data)

class Stack:
    def __init__(self,l = None):
        self.stack = list() if l == None else  l
        self.size = len(self.stack)
    
    def push(self,item):
        self.stack.append(item)
        self.size += 1

    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0 

    def sizes(self):
        return len(self.stack)

class BST:
    def __init__(self, root=None): 
        self.root = None if root == None else root

    def insert(self, data):  
        if self.root == None:
            node = Node(data)
            self.root = node
        else:
            cur = self.root
            while cur != None:
                if data > cur.data:
                    if cur.right == None:
                        node = Node(data)
                        cur.right = node
                        break
                    else:
                        cur = cur.right
                else:
                    if cur.left == None:
                        node = Node(data)
                        cur.left = node
                        break
                    else:
                        cur = cur.left
        return self.root
                
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

def posttotree(postfix):
    s = Stack()
    for ch in postfix:
        if ch not in "+-*/":
            s.push(Node(ch))
        else:
            r = s.pop()
            l = s.pop()
            node = Node(ch, left=l, right=r)
            s.push(node)
    node = s.pop()
    return node

def treetoin(tree):
    if tree is not None:
        if tree.data in "+-*/":
            print("(", end="")
        treetoin(tree.left)
        print(tree, end="")
        treetoin(tree.right)
        if tree.data in "+-*/":
            print(")", end="")

def treetopre(tree):
    if tree is not None:
        print(tree, end="")
        treetopre(tree.left)
        treetopre(tree.right)

inp = input("Enter Postfix : ")
tree = posttotree(inp)
print("Tree :")
printTree90(tree)
print("--------------------------------------------------")
print("Infix : ",end="")
treetoin(tree)
print()
print("Prefix : ",end="")
treetopre(tree)
