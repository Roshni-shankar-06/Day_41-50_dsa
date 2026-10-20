class Solution {
 public:
  void wiggleSort(vector<int>& nums) {
    const int n = nums.size();
    const auto it = nums.begin() + n / 2;
    nth_element(nums.begin(), it, nums.end());
    const int median = *it;

// index-rewiring
