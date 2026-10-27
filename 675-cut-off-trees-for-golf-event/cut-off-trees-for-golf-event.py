class Solution:
  def cutOffTree(self, forest: List[List[int]]) -> int:
    m = len(forest)
    n = len(forest[0])
    
    # Collect all trees: (height, r, c)
    trees = []
    for r in range(m):
      for c in range(n):
        if forest[r][c] > 1:
          trees.append((forest[r][c], r, c))
    
    # Sort trees by height
    trees.sort()
    
    # BFS function to find min steps from (sr, sc) to (tr, tc)
    def bfs(sr, sc, tr, tc):
      if sr == tr and sc == tc:
        return 0
      q = collections.deque([(sr, sc)])
      seen = {(sr, sc)}
      steps = 0
      
      while q:
        steps += 1
        for _ in range(len(q)):
          r, c = q.popleft()
          for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= m or nc < 0 or nc >= n:
              continue
           
   
