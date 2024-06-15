import unittest
from  sort.quick_sort import quick_sort

class TestQuickSort(unittest.TestCase):
    def test_quick_sort(self):
        arr = [2, 5, 4, 8, 9, 1, 3]
        print(quick_sort.quick_sort(arr))

if __name__ == '__main__':
    unittest.main()
