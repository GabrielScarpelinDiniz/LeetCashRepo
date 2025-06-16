class Solution {
    int[] original;
    int[] current;
    
    public Solution(int[] nums) {
        this.original = nums;
        this.current = new int[nums.length];
        System.arraycopy(nums, 0, this.current, 0, nums.length);
    }
    
    public int[] reset() {
        System.arraycopy(this.original, 0, this.current, 0, this.original.length);
        return original;
    }
    
    public int[] shuffle() {
        Random r = new Random();
        for(int i = current.length; i > 0 ; i--){
            int toShuffle = r.nextInt(i);
            int temp = current[i - 1];

            current[i - 1] = current[toShuffle];
            current[toShuffle] = temp;
        }

        return current;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int[] param_1 = obj.reset();
 * int[] param_2 = obj.shuffle();
 */