import unittest

from sorting.insert_sort import sort

class TestInsertSort(unittest.TestCase):
    
    def test_sort_empty_list(self):
        list_to_sort = []

        sort(list_to_sort)

        self.assertEqual(list_to_sort, [])

    def test_sort_does_not_change_sorted_list(self):
        list_to_sort = [1, 2, 3]

        sort(list_to_sort)

        self.assertEqual(list_to_sort, [1, 2, 3])

    def test_sort(self):
        list_to_sort = [3, 1, 2, 9, 5]

        sort(list_to_sort)

        self.assertEqual(list_to_sort, [1, 2, 3, 5 ,9])

    def test_sort_with_duplicates(self):
        list_to_sort = [3, 1, 2, 2, 9, 5]

        sort(list_to_sort)

        self.assertEqual(list_to_sort, [1, 2, 2, 3, 5 ,9])

    def test_sort_two_elements(self):
        list_to_sort = [3, 1]

        sort(list_to_sort)

        self.assertEqual(list_to_sort, [1, 3])


    def test_sort_one_element(self):
        list_to_sort = [1]

        sort(list_to_sort)

        self.assertEqual(list_to_sort, [1])