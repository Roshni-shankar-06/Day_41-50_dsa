class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        
        # Count frequency of each character
        for char in set(s):
            if s.count(char) < k:
                # Split the string by this invalid character and recurse
                return max(self.longestSubstring(sub, k) for sub in s.split(char))
        
        # If every character in the string appears at least k times
        return len(s)
