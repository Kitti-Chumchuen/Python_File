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
    
    def count(self, node):
        r, l = 0, 0
        R = str(node.data)
        L = str(node.data)
        curR = node
        curL = node
        if node != None:
            while curL.left != None:
                L += str(curL.left.data)
                print(l,":",L)
                curL = curL.left
                l += 1
            while curR.right != None:
                R += str(curR.right.data)
                print(r,":",R)
                curR = curR.right
                r += 1
            
        #print("Left :",L)
        #print("Right :",R)
        if r > l:
            return r
        elif r < l:
            return l
        elif r == l:
            return r
        else:
            return -1

    def height(self, node):
        if node == None:
            return 0
        #print(node.data, end=(" "))
        leftH = self.height(node.left)
        rightH = self.height(node.right)
        print(leftH," ",rightH, end=(" "))
        print(max(leftH, rightH))

        return max(leftH, rightH) + 1

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = input('Enter Input : ').split(",")
for i in inp:
    if i[:1] == "i":
        root = T.insert(i[2:])
        print("insert",i[2:])
        T.printTree(root)

#a = T.height(root)
# T.printTree(root)
# print("")
#print("Height of this tree is :",a-1)