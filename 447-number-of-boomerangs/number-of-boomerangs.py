class Solution:
    def numberOfBoomerangs(self, points: list[list[int]]) -> int:
        total_boomerangs = 0
        
        for x1, y1 in points:
            distance_counts = {}
            
            for x2, y2 in points:
                # Calculate squared Euclidean distance to avoid floating-point issues
                dx = x1 - x2
                dy = y1 - y2
                squared_dist = dx * dx + dy * dy
                
                # Count frequencies of each distance from the current anchor
                distance_counts[squared_dist] = distance_counts.get(squared_dist, 0) + 1
            
            # For each unique distance, calculate permutations of picking 2 points
            for count in distance_counts.values():
                if count > 1:
                    total_boomerangs += count * (count - 1)
                    
        return total_boomerangs
