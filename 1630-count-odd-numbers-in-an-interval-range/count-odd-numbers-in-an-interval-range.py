class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # Odd numbers up to high minus odd numbers up to (low - 1)
        return (high + 1) // 2 - low // 2
