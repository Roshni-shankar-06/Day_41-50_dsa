import java.util.*;

class Solution {
    public int[][] outerTrees(int[][] trees) {
        if (trees.length <= 3) {
            return trees;
        }

        // Step 1: Sort by x-coordinate, then by y-coordinate
        Arrays.sort(trees, (a, b) -> a[0] != b[0] ? Integer.compare(a[0], b[0]) : Integer.compare(a[1], b[1]));

        List<int[]> hull = new ArrayList<>();

        // Step 2: Build the lower hull
        for (int[] tree : trees) {
            while (hull.size() >= 2 && crossProduct(hull.get(hull.size() - 2), hull.get(hull.size() - 1), tree) < 0) {
                hull.remove(hull.size() - 1);
            }
            hull.add(tree);
        }

        // Step 3: Build the upper hull
        for (int i = trees.length - 2; i >= 0; i--) {
            int[] tree = trees[i];
            while (hull.size() >= 2 && crossProduct(hull.get(hull.size() - 2), hull.get(hull.size() - 1), tree) < 0) {
                hull.remove(hull.size() - 1);
            }
            hull.add(tree);
        }

        // Step 4: Remove duplicate points using a Set with a coordinate string key
        Set<String> visited = new HashSet<>();
        List<int[]> result = new ArrayList<>();
        
        for (int[] p : hull) {
            String key = p[0] + "," + p[1];
            if (!visited.contains(key)) {
                visited.add(key);
                result.add(p);
            }
        }

        return result.toArray(new int[result.size()][]);
    }

    // Helper method to calculate the cross product of vectors BA and CA
    private int crossProduct(int[] a, int[] b, int[] c) {
        return (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0]);
    }
}

