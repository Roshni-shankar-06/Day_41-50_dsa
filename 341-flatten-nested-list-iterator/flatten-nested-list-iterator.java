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
     ;
  
