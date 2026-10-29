import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> lexicalOrder(int n) {
        List<Integer> result = new ArrayList<>();
        int curr = 1;

        for (int i = 0; i < n; i++) {
            result.add(curr);
            
            // Try to go deeper down the prefix tree (e.g., 1 -> 10 -> 100)
            if (curr * 10 <= n) {
                curr *= 10;
            } else {
                // If we hit the upper limit 'n' or a number ending in 9 (e.g., 19),
                // we must backtrack up the tree by dividing by 10.
                while (curr % 10 == 9 || curr >= n) {
                    curr /= 10;
                }
                // Move to the next sibling (e.g., 11 -> 12)
                curr++;
            }
        }

        return result;
    }
}
