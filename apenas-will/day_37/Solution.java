class Solution {
    List<List<Integer>> sol = new ArrayList<>();
    
    public void backtrack(int[] nums, List<Integer> permutation, boolean[] used){
        if(permutation.size() == nums.length){
            sol.add(new ArrayList<>(permutation));
            return;
        }

        for(int i = 0; i < nums.length; i++){
            if(!used[i]){
                permutation.add(nums[i]);
                used[i] = true;
                backtrack(nums, permutation, used);
                permutation.remove(permutation.size() - 1);
                used[i] = false;
            }
        }
    }
    
    public List<List<Integer>> permute(int[] nums) {
        List<Integer> permutation = new ArrayList<>();
        boolean[] used = new boolean[nums.length];
        backtrack(nums, permutation, used);
        return sol;
    }
}