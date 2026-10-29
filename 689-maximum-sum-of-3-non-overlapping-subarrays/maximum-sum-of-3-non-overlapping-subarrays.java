class Solution {
    public int[] maxSumOfThreeSubarrays(int[] nums, int k) {
        int n = nums.length;
        
        // Tracking variables for rolling window sums
        int currentWindow1Sum = 0;
    
