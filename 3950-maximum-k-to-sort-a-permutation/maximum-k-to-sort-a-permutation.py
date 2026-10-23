from typing import List

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        # Find the maximum possible bitmask (all bits set up to n-1)
        pow2 = 1
        while pow2 < n:
    
