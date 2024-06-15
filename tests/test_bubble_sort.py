import unittest
from sort.bubble_sort import bubble_sort

class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self):
       arr = [2, 5, 4, 8, 9, 1, 3]
       print(bubble_sort.bubble_sort(arr))

if __name__ == '__main__':
    unittest.main()
