class Solution {
  public int findIntegers(int num) {
    StringBuilder bits = new StringBuilder();
    for (; num > 0; num >>= 1)
      bits.append(num & 1);

    final int n = bits.length();
    int[] zero = new int[n];
    int[] one = new int[n];

 
