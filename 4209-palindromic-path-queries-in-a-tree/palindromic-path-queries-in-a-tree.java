import java.util.*;

class Solution {
    private int n;
    private List<Integer>[] adj;
    private int[] parent, depth, heavy, head, pos;
    private int curPos;
    private int[] bit; 
    private int[] nodeValues;

    public List<Boolean> palindromePath(int n, int[][] edges, String s, String[] queries) {
        this.n = n;
        adj = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new ArrayList<>();
        }
        for (int[] e : edges) {
            adj[e[0]].add(e[1]);
            adj[e[1]].add(e[0]);
        }

        parent = new int[n];
        depth = new int[n];
        heavy = new int[n];
        head = new int[n];
        pos = new int[n];
        nodeValues = new int[n];
        Arrays.fill(heavy, -1);

        // Precompute subtree sizes, depths, and heavy edges
        dfs(0, -1, 0);
        curPos = 1; 
        
        // Decompose the tree into heavy chains
        decompose(0, 0);

        // Initialize Fenwick tree with character bitmasks
        bit = new int[n + 1];
        for (int i = 0; i < n; i++) {
            nodeValues[i] = 1 << (s.charAt(i) - 'a');
            updateBit(pos[i], nodeValues[i]);
        }

        List<Boolean> result = new ArrayList<>();
        for (String q : queries) {
            String[] parts = q.split(" ");
            if (parts[0].equals("update")) {
                int u = Integer.parseInt(parts[1]);
                char c = parts[2].charAt(0);
                int newVal = 1 << (c - 'a');
                // XOR out old value, XOR in new value
                updateBit(pos[u], nodeValues[u] ^ newVal);
                nodeValues[u] = newVal;
            } else {
                int u = Integer.parseInt(parts[1]);
                int v = Integer.parseInt(parts[2]);
                int pathXor = queryPath(u, v);
                // At most 1 character with an odd frequency can exist in a palindrome
                result.add(Integer.bitCount(pathXor) <= 1);
            }
        }
        return result;
    }

    private int dfs(int u, int p, int d) {
        parent[u] = p;
        depth[u] = d;
        int size = 1;
        int maxSubtree = 0;
        for (int v : adj[u]) {
            if (v != p) {
                int vSize = dfs(v, u, d + 1);
                size += vSize;
                if (vSize > maxSubtree) {
                    maxSubtree = vSize;
                    heavy[u] = v;
                }
            }
        }
        return size;
    }

    private void decompose(int u, int h) {
        head[u] = h;
        pos[u] = curPos++;
     
