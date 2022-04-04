# Here is how to instatiate a Binary Search Tree
class Node:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value

    def insertNode(self, value):

        if not self.value:
            self.value = value
            return

        if self.value == value:
            return

        if value < self.value:
            if self.left:
                self.left.insert(value)
                return
            self.left = Node(value)
            return

        if self.right:
            self.right.insert(value)
            return
        self.right = Node(value)

    def deleteNode(self, value, root):
        if not root:
            return root

        if root.value > value:
            root.left = deleteNode(self, value, root.left)

        elif root.value < value:
            root.right = deleteNode(self, value, root.right)

        else:
               if root.left is None:
                    temp_value = root.left
                    root = None
                    return temp_value
                
                elif root.right is None:
                    temp_value = root.right
                    root = None
                    return temp_value
                    
                temp_value = root.right
                
                root.value = temp_value.value
                    
                root.right = deleteNode(root.right, self.value)
                
        return Root
