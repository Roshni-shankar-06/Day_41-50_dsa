class Solution {
  public int findRotateSteps(String ring, String key) {
    Map<String, Integer> mem = new HashMap<>();
    return dfs(ring, key, 0, mem) + key.length();
  }

 
