import java.util.Stack;

class Solution {
    public NestedInteger deserialize(String s) {
        // Base Case: If the string doesn't start with '[', it's just a single integer
        if (s == null || s.isEmpty()) return new NestedInteger();
        if (s.charAt(0) != '[') {
            return new NestedInteger(Integer.parseInt(s));
        }

        Stack<NestedInteger> stack = new Stack<>();
        NestedInteger curr = null;
        
        // Pointers to track the start index of any integer token
        int l = 0; 

        for (int r = 0; r < s.length(); r++) {
            char ch = s.charAt(r);

            if (ch == '[') {
                if (curr != null) {
                    stack.push(curr);
                }
                curr = new NestedInteger();
                l = r + 1;
            } else if (ch == ']' || ch == ',') {
                // If there is a number right before this delimiter, parse it
                if (r > l) {
                    int val = Integer.parseInt(s.substring(l, r));
                    curr.add(new NestedInteger(val));
                }
                l = r + 1;

                // If a nested list closes, add it to its outer parent list
                if (ch == ']' && !stack.isEmpty()) {
                    NestedInteger pop = stack.pop();
                    pop.add(curr);
                    curr = pop;
                }
            }
        }

        return curr;
    }
}
