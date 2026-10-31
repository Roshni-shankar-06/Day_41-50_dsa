class Solution:

  def uniquePaths(self, grid: list[list[int]]) -> int:
    MOD = 10**9 + 7
    m, n = len(grid), len(grid[0])
    memo = {}

    def reflect(r, c, direction):
      # Continuously reflect if hitting a mirror
      while 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
        if direction == 'right':
          direction = 'down'
          r += 1
        else:
          direction = 'right'
          c += 1
      return r, c, direction

    def dp(r, c, direction):
      if r == m - 1 and c == n - 1:
        return 1
      if (r, c, direction) in memo:
        return memo[(r, c, direction)]

      total = 0

      # Try moving right
      nr, nc = r, c + 1
      if direction == 'right':
        # If we just came right, standard step is right (unless next is mirror)
        pass

      # Let's check moving right from current state
      next_r, next_c, next_dir = r, c + 1, 'right'
      next_r, next_c, next_dir = reflect(next_r, next_c, next_dir)
      if 0 <= next_r < m and 0 <= next_c < n:
        total = (total + dp(next_r, next_c, next_dir)) % MOD

      # Try moving down
      next_r, next_c, next_dir = r + 1, c, 'down'
      next_r, next_c, next_dir = reflect(next_r, next_c, next_dir)
      if 0 <= next_r < m and 0 <= next_c < n:
        total = (total + dp(next_r, next_c, next_dir)) % MOD

      memo[(r, c, direction)] = total
      return total

    # Start at (0, 0)
    start_r, start_c = 0, 0
    if grid[start_r][start_c] == 1:
      return 0
    return dp(start_r, start_c, 'right')
