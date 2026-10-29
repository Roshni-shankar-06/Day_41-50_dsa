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
              
