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

    def calculate_parse_tree(self):
        left_operand = _process_parse_tree_node(self.left)
        right_operand = _process_parse_tree_node(self.right)

        if self.value == '-':
            return left_operand - right_operand
        if self.value == '+':
            return left_operand + right_operand
        if self.value == '/':
            return left_operand / right_operand
        if self.value == '*':
            return left_operand * right_operand

    def print_parse_tree(self):
        if not self.left:
            # means it's a leaf
            return self.value
        result = []
        result.append('(')
        result.append(self.left.print_parse_tree())
        result.append(self.value)
        result.append(self.right.print_parse_tree())
        result.append(')')
        return ''.join(result)
        
def _process_parse_tree_node(node):
    if node.value.isdigit():
        return int(node.value)
    return node.calculate_parse_tree()

VALID_DIGITS = [str(x) for x in range(9)]
VALID_OPERAIONS = ['-', '+', '/', '*']

def build_child_parse_tree_value(operand):
    return Tree(''.join(operand))

def process_sub_parse_tree(root, expression, position):
    child = build_parse_tree(expression, position - 1)
    if not root.left:
        root.left = child
    else:
        root.right = child

def build_parse_tree(expression, position = 0):

    root = None
    operand = []
    
    while (position < len(expression) and
           (not root or not root.left or not root.right)):
        symbol = expression[position]
        position += 1
        if symbol == '(':
            if root:
                process_sub_parse_tree(root, expression, position)
            else:
                # create new tree node
                # set value as None as we don't know what the value is going to be yet
                root = Tree(None)
        if symbol in VALID_DIGITS:
            operand.append(symbol)
        if symbol in VALID_OPERAIONS:
            root.left = build_child_parse_tree_value(operand)
            root.value = symbol
            operand = []
        if symbol == ')':
            root.right = build_child_parse_tree_value(operand)
            operand = []
    return root

