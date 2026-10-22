import java.util.*;

public class NestedIterator implements Iterator<Integer> {
    // Stack holds individual elements instead of iterators
    private Stack<NestedInteger> stack;

    public NestedIterator(List<NestedInteger> nestedList) {
        stack = new Stack<>();
        prepareStack(nestedList);
    }

    @Override
    public Integer next() {
        if (!hasNext()) {
            throw new NoSuchElementException();
        }
        return stack.pop().getInteger();
    }

    @Override
    public boolean hasNext() {
        // Flatten nested lists on-demand until an integer is on top
        while (!stack.isEmpty() && !stack.peek().isInteger()) {
            List<NestedInteger> nextList = stack.pop().getList();
            prepareStack(nextList);
        }
        return !stack.isEmpty();
    }

    // Helper method to push items in reverse order
    private void prepareStack(List<NestedInteger> list) {
        for (int i = list.size() - 1; i >= 0; i--) {
            stack.push(list.get(i));
        }
    }
}

