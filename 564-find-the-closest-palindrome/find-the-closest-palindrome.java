import java.util.*;

class Solution {
    public String nearestPalindromic(String n) {
        long num = Long.parseLong(n);
        int len = n.length();
        
        // Step 1: Handle base structural edge candidates
        List<Long> candidates = new ArrayList<>();
        candidates.add((long) Math.pow(10, len - 1) - 1); // Edge case: e.g., 999
        candidates.add((long) Math.pow(10, len) + 1);     // Edge case: e.g., 10001
        
        // Step 2: Generate candidates from the prefix
        long prefix = Long.parseLong(n.substring(0, (len + 1) / 2));
        long[] prefixOffsets = {prefix, prefix + 1, prefix - 1};
        
        for (long p : prefixOffsets) {
            StringBuilder sb = new StringBuilder(String.valueOf(p));
            String reversed = new StringBuilder(sb).reverse().toString();
            if (len % 2 == 0) {
                sb.append(reversed);
            } else {
                sb.append(reversed.substring(1));
            }
            candidates.add(Long.parseLong(sb.toString()));
        }
        
        // Step 3: Find the closest valid distinct palindrome
        long minDiff = Long.MAX_VALUE;
        long result = 0;
        
        for (long cand : candidates) {
            if (cand == num) continue; // Must be distinct
            
            long diff = Math.abs(cand - num);
            if (diff < minDiff) {
                minDiff = diff;
                result = cand;
            } else if (diff == minDiff) {
                result = Math.min(result, cand); // Tie-breaker: smaller value
            }
        }
        
        return String.valueOf(result);
    }
}
