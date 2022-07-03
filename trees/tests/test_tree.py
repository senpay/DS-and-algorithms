import unittest

from trees.tree import Tree

# Make test tree like the one in Read
# Root node:

root = Tree

class TestTree(unittest.TestCase):
    
    def test_sort_empty_list(self):
        list_to_sort = []

        sort(list_to_sort)