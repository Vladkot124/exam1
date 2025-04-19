import unittest
from main import filter_and_sort_positive

class TestFilterAndSortPositive(unittest.TestCase):
    def test_positive_filter_and_sort(self):
        data = [1, -5, 2, 0, 6, 8, 3]
        expected = [1, 2, 3, 6, 8]
        self.assertEqual(filter_and_sort_positive(data), expected)

    def test_all_negative(self):
        data = [-1, -2, -3]
        expected = []
        self.assertEqual(filter_and_sort_positive(data), expected)

    def test_empty_list(self):
        data = []
        expected = []
        self.assertEqual(filter_and_sort_positive(data), expected)

    def test_all_positive_unsorted(self):
        data = [5, 1, 4, 3]
        expected = [1, 3, 4, 5]
        self.assertEqual(filter_and_sort_positive(data), expected)

if __name__ == '__main__':
    unittest.main()