import unittest

from BinaryIndexedTree import BinaryIndexedTree

class SimpleTests(unittest.TestCase):
    def setUp(self):
        self.bit = BinaryIndexedTree(16)

        self.bit.Set(1, 1)
        self.bit.Set(2, 0)
        self.bit.Set(3, 2)
        self.bit.Set(4, 1)
        self.bit.Set(5, 1)
        self.bit.Set(6, 3)
        self.bit.Set(7, 0)
        self.bit.Set(8, 4)
        self.bit.Set(9, 2)
        self.bit.Set(10, 5)
        self.bit.Set(11, 2)
        self.bit.Set(12, 2)
        self.bit.Set(13, 3)
        self.bit.Set(14, 1)
        self.bit.Set(15, 0)
        self.bit.Set(16, 2)

    def testSum(self):
        self.assertTrue(self.bit.tree[9]==2)
        self.assertTrue(self.bit.Sum(10) ==19)

if __name__ == '__main__':
    unittest.main()
