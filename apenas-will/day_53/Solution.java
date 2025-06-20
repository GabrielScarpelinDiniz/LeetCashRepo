class Solution {
    Map<Integer, List<Integer>> indexes = new HashMap<>();
    public Solution(int[] nums) {
        for(int i = 0; i < nums.length; i++){
            this.indexes.putIfAbsent(nums[i], new ArrayList<>());
            this.indexes.get(nums[i]).add(i);
        }
    }
    
    public int pick(int target) {
        Random r = new Random();
        int i = r.nextInt(this.indexes.get(target).size());
        return this.indexes.get(target).get(i);
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int param_1 = obj.pick(target);
 */