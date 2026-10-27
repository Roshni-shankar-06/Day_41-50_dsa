class Solution:
  def cutOffTree(self, forest: List[List[int]]) -> int:
    m = len(forest)
    n = len(forest[0])
    
    # Collect all trees: (height, r, c)
    trees = []
 
