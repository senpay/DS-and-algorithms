import unittest

from merge_sort import merge

class TestMergeSort(unittest.TestCase):
    
    def test_merge_two_empty_list(self):
        first_list = []
        second_list = []

        result = merge(first_list, second_list)

        self.assertEqual(result, [])

    def test_merge_empty_list_and_not_empty(self):
        first_list = []
        second_list = [1]

        result = merge(first_list, second_list)

        self.assertEqual(result, second_list)

    def test_merge_not_empty_list_and_empty(self):
        first_list = [1]
        second_list = []

        result = merge(first_list, second_list)

        self.assertEqual(result, first_list)

    def test_merge_two_one_element_lists(self):
        first_list = [2]
        second_list = [1]

        result = merge(first_list, second_list)

        self.assertEqual(result, [1, 2])


    def test_merge_two_sorted_lists(self):
        first_list = [2, 4, 10]
        second_list = [1, 2, 3, 17, 21]

        result = merge(first_list, second_list)

        self.assertEqual(result, [1, 2, 2, 3, 4, 10, 17, 21])