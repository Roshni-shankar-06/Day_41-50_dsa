class Solution {
  public String removeDuplicateLetters(String s) {
    StringBuilder sb = new StringBuilder();
    int[] count = new int[128];

