class Solution:
    def containVirus(self, isInfected: list[list[int]]) -> int:
        R, C = len(isInfected), len(isInfected[0])
        total_walls = 0
        
        while True:
            # 1. Track components and information for the current day
            visited = [[False] * C for _ in range(R)]
            regions = []       # Coordinates of infected cells in each region
            frontiers = []     # Set of unique uninfected cells threatened by each region
            walls_needed = []  # Total perimeter walls needed for each region
            
            for r in range(R):
                for c in range(C):
                    if isInfected[r][c] == 1 and not visited[r][c]:
                        # Explore the current unquarantined viral component
                        region = []
                        frontier = set()
                        walls = 0
                        
                        # Iterative DFS to find connected component
                        stack = [(r, c)]
                        visited[r][c] = True
                        
                        while stack:
                            curr_r, curr_c = stack.pop()
                            region.append((curr_r, curr_c))
                            
                            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                                nr, nc = curr_r + dr, curr_c + dc
                                if 0 <= nr < R and 0 <= nc < C:
                                    if isInfected[nr][nc] == 1:
                                        if not visited[nr][nc]:
                                            visited[nr][nc] = True
                                            stack.append((nr, nc))
                                    elif isInfected[nr][nc] == 0:
                                        # Every adjacent uninfected cell requires a wall
                                        walls += 1
                                        frontier.add((nr, nc))
                                        
                        if region:
                            regions.append(region)
                            frontiers.append(frontier)
                            walls_needed.append(walls)
            
            # If no regions are threatening any uninfected cells, we are done
            if not regions or all(not f for f in frontiers):
                break
                
            # 2. Greedy Choice: Identify the most threatening region
            # We select the index of the region with the largest unique frontier size
            target_idx = max(range(len(frontiers)), key=lambda i: len(frontiers[i]))
            
            # Accumulate the perimeter wall count needed to quarantine it
            total_walls += walls_needed[target_idx]
            
            # 3. Quarantine the targeted region (mark as -1 so it stays inactive)
            for r, c in regions[target_idx]:
                isInfected[r][c] = -1
                
            # 4. Simulate viral spread for all remaining non-quarantined regions
            for i, region in enumerate(regions):
                if i == target_idx:
                    continue
                for r, c in frontiers[i]:
                    isInfected[r][c] = 1
                    
        return total_walls
