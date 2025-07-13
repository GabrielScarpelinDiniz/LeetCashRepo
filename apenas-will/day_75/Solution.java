class Solution {
    public void backtracking(List<List<Integer>> res, int[] nums, List<Integer> subset, int start){
        res.add(new ArrayList<>(subset));

        for(int i = start; i < nums.length; i ++){
            subset.add(nums[i]);
            backtracking(res, nums, subset, i + 1);
            subset.remove(subset.size() - 1);
        }
    }
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        backtracking(res, nums, new ArrayList<>(), 0);
        return res;
    }
}