class Solution {
  public String removeDuplicateLetters(String s) {
    StringBuilder sb = new StringBuilder();
    int[] count = new int[128];
    boolean[] used = new boolean[128];

    for (final char c : s.toCharArray())
      ++count[c];

    for (final char c : s.toCharArray()) {
    
      
