class Solution {
 public:
  int coinChange(vector<int>& coins, int amount) {
    // dp[i] := the minimum number of coins to make up i
    vector<int> dp(amount + 1, amount + 1);
   
