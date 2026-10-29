class Solution {
    public int[] runningSum(int[] nums) {
        // Start from the second element and accumulate the previous value
        for (int i = 1; i < nums.length; i++) {
            nums[i] += nums[i - 1];
        }
        return nums;
    }
}
