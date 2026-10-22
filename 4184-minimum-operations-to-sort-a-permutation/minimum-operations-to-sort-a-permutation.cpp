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
         
