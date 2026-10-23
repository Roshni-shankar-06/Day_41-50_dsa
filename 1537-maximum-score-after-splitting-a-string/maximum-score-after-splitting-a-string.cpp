class Solution {
 public:
  int maxScore(string s) {
    int ans = 0;
    int zeros = 0;
    int ones = ranges::count(s, '1');
