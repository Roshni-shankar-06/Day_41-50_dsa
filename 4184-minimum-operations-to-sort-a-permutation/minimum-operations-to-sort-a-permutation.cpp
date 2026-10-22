#include <vector>
#include <algorithm>

class Solution {
public:
    int minOperations(std::vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) return 0;

        // Find the index of 0
        int zero = 0;
        for (int i = 0; i < n; ++i) {
            if (nums[i] == 0) {
                zero = i;
                break;
            }
        }

        bool right_inc = true;
        bool left_inc = true;

        // Check both cyclic directions
        for (int i = 1; i < n; ++i) {
            if (nums[(zero + i) % n] != i) {
                right_inc = false;
            }
            if (nums[(zero - i + n) % n] != i) {
                left_inc = false;
            }
        }

        int ans = 1e9;

        // Case 1: Elements increase to the right from 0
        if (right_inc) {
            // Path A: Shift left directly to bring 0 to the front
            ans = std::min(ans, zero);
            // Path B: Reverse -> Shift left -> Reverse back
            ans = std::min(ans, 2 + n - zero);
        }

        // Case 2: Elements increase to the left from 0 (decreasing sequence)
        if (left_inc) {
            // Path C: Shift left to move 0 to the end -> Reverse
            ans = std::min(ans, zero + 2);
            // Path D: Reverse -> Shift left to bring 0 to the front
        
