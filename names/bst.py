class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
             if not self.left:
                self.left = BSTNode(value)
             else:
                 self.left.insert(value)
        else:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            if not self.left:
                return False
            return self.left.contains(target) #Goes to the left node of the tree
        else:
            if not self.right:
                return False
            return self.right.contains(target) #Goes to the right node of the tree

    # Return the maximum value found in the tree
    def get_max(self): #Looks at the right side of th tree for max value
        if not self:
            return None
        if not self.right:
            return self.value
         #It keeps going until it gets the max
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            node.left.in_order_print(node.left)
            print(node.value)
        if node.right:
            node.right.in_order_print(node.right)
            print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        #Create a queue
        queue = deque()
        queue.append(node)

        while len(queue) > 0:
            current = queue.popleft()

            print(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
