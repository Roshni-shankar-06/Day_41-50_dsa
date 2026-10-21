class Solution:
    def minOperations(self, s: str) -> int:
        if s == ''.join(sorted(s)):
            return 0

        n = len(s)

        if n == 2:
            return -1

        if s[0] == min(s) or s[-1] == max(s):
            return 1

          
    
  
      

  
       
        
   
         


 
