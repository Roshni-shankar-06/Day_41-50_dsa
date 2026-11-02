class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        # Step 1: Sort the array to easily find the median
        nums.sort()
        
        # Step 2: Identify the median element
        median = nums[len(nums) // 2]
        
        # Step 3: Sum the absolute differences between each number and the median
        return sum(abs(num - median) for num in nums)
