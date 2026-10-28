#include <vector>
#include <bitset>
#include <algorithm>

class Solution {
public:
    int minCost(std::vector<std::vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size(); // Fix: ensure we use grid[0].size() for column count
        
        // dp[j] holds bits for reachable XOR configurations in column j
        std::vector<std::bitset<1024>> dp(n);
        
        // Initialize top-left cell
        dp[0].set(grid[0][0]);
        
        // Process first row
        for (int j = 1; j < n; ++j) {
            for (int mask = 0; mask < 1024; ++mask) {
                if (dp[j - 1].test(mask)) {
                    dp[j].set(mask ^ grid[0][j]);
                }
            }
        }
        
        // Process the rest of the grid
        for (int i = 1; i < m; ++i) {
            std::vector<std::bitset<1024>> next_dp(n);
            
            // First column transitions from above
            for (int mask = 0; mask < 1024; ++mask) {
                if (dp[0].test(mask)) {
                    next_dp[0].set(mask ^ grid[i][0]);
                }
            }
            
            // Other columns transition from left and above
            for (int j = 1; j < n; ++j) {
                std::bitset<1024> combined = dp[j] | next_dp[j - 1];
                for (int mask = 0; mask < 1024; ++mask) {
                    if (combined.test(mask)) {
                        next_dp[j].set(mask ^ grid[i][j]);
                    }
                }
            }
            dp = std::move(next_dp);
        }
        
        // Scan for the smallest set bit in the destination cell
        for (int mask = 0; mask < 1024; ++mask) {
            if (dp[n - 1].test(mask)) {
                return mask;
            }
        }
        
        return -1;
    }
};
