# A single node of a singly linked list
class Node:
  # constructor
  def __init__(self, data, next): 
    self.data = data
    self.next = next

# Creating a single node
first = Node(3,4)
print(first.data)
print(first.next)