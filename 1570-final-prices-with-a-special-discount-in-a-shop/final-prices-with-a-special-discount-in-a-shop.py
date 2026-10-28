class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        stack = [] # Stores indices of elements
        
        for i in range(len(prices)):
            # While stack is not empty and current price is less than or equal 
            # to the price of the index at the top of the stack
            while stack and prices[i] <= prices[stack[-1]]:
                prev_idx = stack.pop()
                prices[prev_idx] -= prices[i] # Apply the discount
                
            stack.append(i) # Push current index onto the stack
            
        return prices
