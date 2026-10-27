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
            if forest[nr][nc] == 0 or (nr, nc) in seen:
              continue
            if nr == tr and nc == tc:
              return steps
            q.append((nr, nc))
            seen.add((nr, nc))
      return -1

    ans = 0
    curr_r, curr_c = 0, 0
    
    for _, tr, tc in trees:
      steps = bfs(curr_r, curr_c, tr, tc)
      if steps == -1:
        return -1
      ans += steps
      curr_r, curr_c = tr, tc
      
    return ans
