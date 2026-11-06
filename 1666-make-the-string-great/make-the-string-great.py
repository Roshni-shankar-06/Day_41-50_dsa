class Solution:

    def makeGood(self, s: str) -> str:
        stack = []

        for char in s:
            # Check if stack is not empty and characters make a bad pair
            if stack and abs(ord(stack[-1]) - ord(char)) == 32:
                stack.pop()  # Remove the matching bad pair character
            else:
                stack.append(char)  # Keep the character

        return "".join(stack)
