class Solution {
public:
    int sortableIntegers(vector<int>& nums) {
        int n = nums.size();

        vector<int> prefMax(n + 1, 0);
        vector<int> suffMin(n + 1, 1000000000);
        vector<int> drops(n, 0);

        for (int i = 0; i < n; i++)
            prefMax[i + 1] = max(prefMax[i], nums[i]);

        for (int i = n - 1; i >= 0; i--)
            suffMin[i] = min(nums[i], suffMin[i + 1]);

        for (int i = 1; i < n; i++)
            drops[i] = drops[i - 1] + (nums[i - 1] > nums[i]);


            for (int d : {k, n / k}) {
                if (d != k && d == k) continue;

          
