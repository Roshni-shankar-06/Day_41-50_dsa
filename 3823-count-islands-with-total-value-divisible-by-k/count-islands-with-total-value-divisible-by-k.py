class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        island_count = 0
        
        # Directions for 4-directional movement (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for r in range(m):
            for c in range(n):
                # If we hit an unvisited land cell (positive value)
                if grid[r][c] > 0:
                    island_sum = 0
                    stack = [(r, c)]
                    
                    # Accumulate the value of the initial cell and "sink" it to avoid repeating
                    island_sum += grid[r][c]
                    grid[r][c] = 0 
                    
                    # Iterative DFS to traverse the island
                    while stack:
                        curr_r, curr_c = stack.pop()
                        
                        for dr, dc in directions:
                            nr, nc = curr_r + dr, curr_c + dc
                            
                            # Check boundaries and if the next cell is valid land
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                                island_sum += grid[nr][nc]
                                grid[nr][nc] = 0  # Mark as visited
                                stack.append((nr, nc))
                    
                    # Check if the total island value is divisible by k
                    if island_sum % k == 0:
                        island_count += 1
                        
        return island_count
