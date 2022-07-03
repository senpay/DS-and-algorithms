import unittest

from trees.tree import Tree

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