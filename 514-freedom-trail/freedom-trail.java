class Solution {
  public int findRotateSteps(String ring, String key) {
    Map<String, Integer> mem = new HashMap<>();
    return dfs(ring, key, 0, mem) + key.length();
  }

  // Returns the number of rotates of ring to match key[index..n).
  private int dfs(final String ring, final String key, int index, Map<String, Integer> mem) {
    if (index == key.length())
      return 0;
    // Add the index to prevent duplication.
    final String hashKey = ring + index;
    if (mem.containsKey(hashKey))
      return mem.get(hashKey);

    int ans = Integer.MAX_VALUE;

   

 
