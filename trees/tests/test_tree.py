import unittest

from trees.tree import Tree, build_parse_tree

# Make test tree like the one in Read
d = Tree('d')
e = Tree('e')
b = Tree('b', d, e)
f = Tree('f')
g = Tree('g')
c = Tree('c', f, g)
a = Tree('a', b, c)

class TestTree(unittest.TestCase):
    
    def test_preorder(self):
        nodes_values = a.preorder_traversal()
        self.assertEqual(nodes_values, ['a', 'b', 'd', 'e', 'c', 'f', 'g'])


    def test_inorder(self):
        nodes_values = a.inorder_traversal()
        self.assertEqual(nodes_values, ['d', 'b', 'e', 'a', 'f', 'c', 'g'])

    def test_postorder(self):
        nodes_values = a.postorder_traversal()
        self.assertEqual(nodes_values, ['d', 'e', 'b', 'f', 'g', 'c', 'a'])

    def test_build_parse_tree_from_simple_expression(self):
        expression = ' ( 12 + 21 )'

        tree = build_parse_tree(expression)

        self.assertEqual(tree.value, '+')
        self.assertEqual(tree.left.value, '12')
        self.assertEqual(tree.right.value, '21')

    def test_build_parse_tree_from_nested_expression(self):
        expression = ' ( 12 * (56 - 2) )'

        tree = build_parse_tree(expression)

        self.assertEqual(tree.value, '*')
        self.assertEqual(tree.left.value, '12')
        self.assertEqual(tree.right.value, '-')
        self.assertEqual(tree.right.left.value, '56')
        self.assertEqual(tree.right.right.value, '2')

    def test_calculate_parse_tree_value(self):

        expression = ' ( 12 * (56 - 2) )'

        tree = build_parse_tree(expression)

        result = tree.calculate_parse_tree()

        self.assertEqual(result, 648)

    def test_print_parse_tree(self):
        expression = ' ( 12 * (56 - 2) )'

        parse_tree = build_parse_tree(expression)

        result = parse_tree.print_parse_tree()

        self.assertEqual(result, '(12*(56-2))')