class Solution:
  def cutOffTree(self, forest: List[List[int]]) -> int:
    m = len(forest)
    n = len(forest[0])
    
    # Collect all trees: (height, r, c)
    trees = []
    for r in range(m):
      for c in range(n):
        if forest[r][c] > 1:
         
