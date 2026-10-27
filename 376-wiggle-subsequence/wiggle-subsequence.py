class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        increasing = 1
        decreasing = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                increasing = decreasing + 1
            elif nums[i] < nums[i - 1]:
                decreasing = increasing + 1
        return max(increasing, decreasing)
