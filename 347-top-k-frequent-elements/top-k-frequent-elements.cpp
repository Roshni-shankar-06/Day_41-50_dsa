struct T {
  int num;
  int freq;
};

class Solution {
 public:
  vector<int> topKFrequent(vector<int>& nums, int k) {
    const int n = nums.size();
    vector<int> ans;
    unordered_map<int, int> count;
   
