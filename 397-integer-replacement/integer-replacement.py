class Solution:
    def integerReplacement(self, n: int) -> int:
        moves = 0
        while n > 1:
            if n % 2 == 0:
                n //= 2
            elif n == 3 or (n & 3) == 1:
                # n % 4 == 1 or n == 3 -> subtract 1
                n -= 1
            else:
                # n % 4 == 3 -> add 1
                n += 1
            moves += 1
        return moves
