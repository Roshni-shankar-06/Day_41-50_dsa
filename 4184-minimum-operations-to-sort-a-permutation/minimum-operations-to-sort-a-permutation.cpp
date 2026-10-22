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
             
