import java.util.Random;

class Solution {
    private final int[] original;
    private int[] array;
    private final Random rand;

    public Solution(int[] nums) {
        this.array = nums;
        this.original = nums.clone();
        this.rand = new Random();
    }
    
    /** Resets the array to its original configuration and returns it. */
    public int[] reset() {
        this.array = this.original.clone();
        return this.array;
    }
    
    /** Returns a random shuffling of the array. */
    public int[] shuffle() {
        // Implement the Fisher-Yates shuffle
        for (int i = array.length - 1; i > 0; i--) {
            // Pick a random index from 0 to i (inclusive)
            int j = rand.nextInt(i + 1);
            
            // Swap elements at i and j
            int temp = array[i];
            array[i] = array[j];
            array[j] = temp;
        }
        return array;
    }
}
