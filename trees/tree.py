class Tree:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def preorder_traversal(self, nodes_values=[]):
        nodes_values.append(self.value)
        if self.left:
            self.left.preorder_traversal(nodes_values)
        if self.right:
            self.right.preorder_traversal(nodes_values)
        return nodes_values


    def inorder_traversal(self, nodes_values=[]):
        if self.left:
            self.left.inorder_traversal(nodes_values)
        nodes_values.append(self.value)
        if self.right:
            self.right.inorder_traversal(nodes_values)
        return nodes_values


    def postorder_traversal(self, nodes_values=[]):
        if self.left:
            self.left.postorder_traversal(nodes_values)
        if self.right:
            self.right.postorder_traversal(nodes_values)
        nodes_values.append(self.value)
        return nodes_values