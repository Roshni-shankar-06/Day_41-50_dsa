class Solution {
  public int findIntegers(int num) {
    StringBuilder bits = new StringBuilder();
    for (; num > 0; num >>= 1)
      bits.append(num & 1);


