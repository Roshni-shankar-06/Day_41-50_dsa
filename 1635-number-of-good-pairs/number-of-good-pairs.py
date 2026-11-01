class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = {}
        good_pairs = 0
        
        for num in nums:
            if num in count:
                # Add the number of times we've seen this element before
                good_pairs += count[num]
                count[num] += 1
            else:
                count[num] = 1
                
        return good_pairs
