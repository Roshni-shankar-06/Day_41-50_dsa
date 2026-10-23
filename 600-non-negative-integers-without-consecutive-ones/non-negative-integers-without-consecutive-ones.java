class Solution {
  public int findIntegers(int num) {
    StringBuilder bits = new StringBuilder();
    for (; num > 0; num >>= 1)
      bits.append(num & 1);

    final int n = bits.length();
    int[] zero = new int[n];
    int[] one = new int[n];

    zero[0] = 1;
    one[0] = 1;

    for (int i = 1; i < n; ++i) {
      zero[i] = zero[i - 1] + one[i - 1];
    
