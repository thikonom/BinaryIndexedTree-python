class BinaryIndexedTree(object):
    def __init__(self, max_val):
        self.sz = max_val
        self.tree = [0]*(self.sz + 1)

    def Set(self, idx, val):
        """
        Updates the value of index idx to val.
        """
        while idx <= self.sz:
            self.tree[idx] += val
            idx += (idx & -idx)

    def Sum(self, idx):
        """
        Returns the sum of all values from index 1 to index i (inclusive). 
        """
        curr_sum = 0
        while idx:
            curr_sum += self.tree[idx]
            idx -= (idx & -idx)
        return curr_sum
