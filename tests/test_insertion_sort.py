import unittest
from sort.insertion_sort import insertion_sort

class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        arr = [2, 5, 4, 8, 9, 1, 3]
        print(insertion_sort.insertion_sort(arr))

if __name__ == '__main__':
    unittest.main()
