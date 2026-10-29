class Solution {
    public int[] maxSumOfThreeSubarrays(int[] nums, int k) {
        int n = nums.length;
        
        // Tracking variables for rolling window sums
        int currentWindow1Sum = 0;
        int currentWindow2Sum = 0;
        int currentWindow3Sum = 0;
        
        // Track the maximum historical configurations
        int maxWindow1Sum = 0;
        int maxWindow12Sum = 0;
        int maxTotalSum = 0;
        
        
