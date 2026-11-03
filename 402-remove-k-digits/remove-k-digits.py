class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        # Step 1 & 2: Build a monotonic increasing stack
        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
            
        # Step 3: If k is still greater than 0, remove from the end
        if k > 0:
            stack = stack[:-k]
            
        # Step 4: Join and strip leading zeros
        res = "".join(stack).lstrip("0")
        
        # Step 5: If string is empty, return "0"
        return res if res else "0"
