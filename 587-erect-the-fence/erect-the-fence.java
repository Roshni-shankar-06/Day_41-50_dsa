import java.util.*;

class Solution {
    public int[][] outerTrees(int[][] trees) {
        if (trees.length <= 3) {
            return trees;
        }

        // Step 1: Sort by x-coordinate, then by y-coordinate
        Arrays.sort(trees, (a, b) -> a[0] != b[0] ? Integer.compare(a[0], b[0]) : Integer.compare(a[1], b[1]));

        List<int[]> hull = new ArrayList<>();
