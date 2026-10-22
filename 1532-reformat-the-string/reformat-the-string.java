class Solution {
    public String reformat(String s) {
        StringBuilder letters = new StringBuilder();
        StringBuilder digits = new StringBuilder();
        
        // Step 1: Separate letters and digits
        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {
                digits.append(c);
            } else {
                letters.append(c);
            }
        }
        
        int lLen = letters.length();
        int dLen = digits.length();
        
        // Step 2: Validate feasibility
        if (Math.abs(lLen - dLen) > 1) {
            return "";
        }
        
        // Step 3: Interleave starting with the larger group
        StringBuilder result = new StringBuilder();
        boolean pickLetter = lLen >= dLen;
        int lIdx = 0, dIdx = 0;
        
        for (int i = 0; i < s.length(); i++) {
            if (pickLetter) {
                result.append(letters.charAt(lIdx++));
            } else {
                result.append(digits.charAt(dIdx++));
            }
            pickLetter = !pickLetter; // Alternate choice
        }
        
        return result.toString();
    }
}

