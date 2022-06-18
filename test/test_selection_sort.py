import unittest

from selection_sort import sort

class TestSelectCopySort(unittest.TestCase):
    
    def test_sort_empty_list(self):
        list_to_sort = []

        sort(list_to_sort)

        self.assertEqual(list_to_sort, [])

    def test_sort_does_not_change_sorted_list(self):
        list_to_sort = [1, 2, 3]

        sorted_list = sort(list_to_sort)

        self.assertEqual(list_to_sort, [1, 2, 3])

    def test_sort(self):
        list_to_sort = [3, 1, 2, 9, 5]

        sorted_list = sort(list_to_sort)

        self.assertEqual(list_to_sort, [1, 2, 3, 5 ,9])