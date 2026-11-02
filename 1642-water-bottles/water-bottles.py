class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_drunk = numBottles
        empty_bottles = numBottles
        
        while empty_bottles >= numExchange:
            # Exchange empty bottles for new full bottles
            new_full = empty_bottles // numExchange
            # Keep track of leftover empty bottles that couldn't be exchanged
            leftover = empty_bottles % numExchange
            
            total_drunk += new_full
            # Your new empty count is the new bottles drunk + the leftovers
            empty_bottles = new_full + leftover
            
        return total_drunk
