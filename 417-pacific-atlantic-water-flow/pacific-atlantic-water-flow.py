class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights or not heights[0]:
            return []
            
        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        
        def dfs(r, c, visited, prev_height):
            # Check boundaries, visited state, and height restriction (must flow uphill)
            if (r < 0 or r >= ROWS or 
                c < 0 or c >= COLS or 
                (r, c) in visited or 
                heights[r][c] < prev_height):
                return
                
            visited.add((r, c))
            
            # Explore all 4 orthogonal directions
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        # Step 1: Run DFS for the top and bottom rows
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])         # Top row (Pacific)
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c]) # Bottom row (Atlantic)
            
        # Step 2: Run DFS for the left and right columns
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])         # Left col (Pacific)
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1]) # Right col (Atlantic)
            
        # Step 3: Find intersection of both reachable sets
        return [list(cell) for cell in pacific if cell in atlantic]
