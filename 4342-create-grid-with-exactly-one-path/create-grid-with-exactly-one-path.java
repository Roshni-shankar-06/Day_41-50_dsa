class Solution {
    public String[] createGrid(int m, int n) {
        char[][] g = new char[m][n];
        for (int i = 0; i < m; i++) {
            Arrays.fill(g[i], '#');
        }
        Arrays.fill(g[0], '.');
        for (int i = 0; i < m; i++) {
         
