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
        bestWindow2Index2 = k;
        result[0] = 0; result[1] = k; result[2] = 2 * k;
        
        // Slide all three windows forward simultaneously
        int w1Start = 1;
        int w2Start = k + 1;
        int w3Start = 2 * k + 1;
        
        while (w3Start <= n - k) {
            // Update rolling sum bounds for each window
            currentWindow1Sum = currentWindow1Sum - nums[w1Start - 1] + nums[w1Start + k - 1];
            currentWindow2Sum = currentWindow2Sum - nums[w2Start - 1] + nums[w2Start + k - 1];
            currentWindow3Sum = currentWindow3Sum - nums[w3Start - 1] + nums[w3Start + k - 1];
            
            // Check if the current Window 1 sets a new maximum sum bound
            if (currentWindow1Sum > maxWindow1Sum) {
                maxWindow1Sum = currentWindow1Sum;
                bestWindow1Index = w1Start;
            }
            
            // Check if Window 1 + Window 2 combination beats historical records
            if (maxWindow1Sum + currentWindow2Sum > maxWindow12Sum) {
              
            // Check if full three-window combination achieves the definitive maximum sum
            if (maxWindow12Sum + currentWindow3Sum > maxTotalSum) {
                maxTotalSum = maxWindow12Sum + currentWindow3Sum;
              
