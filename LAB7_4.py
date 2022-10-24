class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, node, data):
        nn = Node(data)

        if node == None:
            node = nn

        else:
            cur = node
            while cur != None:
                if int(cur.data) > int(data):
                    if cur.left == None:
                        cur.left = nn
                        break
                    else:
                        cur = cur.left

                if int(cur.data) < int(data):
                    if cur.right == None:
                        cur.right = nn
                        break
                    else:
                        cur = cur.right

                if int(cur.data) == int(data):
                    if cur.left == None:
                        cur.left = nn
                        break
                    else:
                        cur = cur.left
        return node

    def minNode(self, node):
        cur = node
        while(cur.left is not None):
            cur = cur.left

        return cur

    def delete(self, node, item):

        if node == None :
            print("Error! Not Found DATA")
            return 

        if (item < node.data):
            node.left = self.delete(node.left, item)

        elif (item > node.data):
            node.right = self.delete(node.right, item)

        elif (item == node.data):

            if node.left is None:
                temp = node.right
                node = None
                return temp

            if node.right is None:
                temp = node.left
                node = None
                return temp

            temp = self.minNode(node.right)
            node.data = temp.data
            node.right = self.delete(node.right, temp.data)

        return node


def printTree90(node, level=0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

#------------------ Program --------------------- #

T = BinarySearchTree()
inp = input('Enter Input : ').split(",")

root = None
n = 0

for i in inp:
    
    a = i.split(" ")

    if str(a[0]) == "i":
        print("insert", int(a[1]))
        root = T.insert(root, int(a[1]))
        printTree90(root)

    elif str(a[0]) == "d":
        print("delete", int(a[1]))
        root = T.delete(root, int(a[1]))
        printTree90(root)   