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
        
        // Tracking the indices corresponding to max configurations
        int bestWindow1Index = 0;
        int bestWindow2Index1 = 0, bestWindow2Index2 = 0;
        int[] result = new int[3];
        
        // Base initialization for the first window positions
        for (int i = 0; i < k; i++) currentWindow1Sum += nums[i];
        for (int i = k; i < 2 * k; i++) currentWindow2Sum += nums[i];
        for (int i = 2 * k; i < 3 * k; i++) currentWindow3Sum += nums[i];
        
        maxWindow1Sum = currentWindow1Sum;
        maxWindow12Sum = currentWindow1Sum + currentWindow2Sum;
        maxTotalSum = maxWindow12Sum + currentWindow3Sum;
        
        bestWindow1Index = 0;
        bestWindow2Index1 = 0;
     
