class Solution {
    public void backtracking(List<List<Integer>> res, int sum, int target, int[] candidates, List<Integer> comb, int start){
        if(sum == target){
            res.add(new ArrayList<>(comb));
            return;
        }

        for(int i = start; i < candidates.length; i++){       
            if(sum + candidates[i] <= target){
                comb.add(candidates[i]);
                backtracking(res, sum + candidates[i], target, candidates, comb, i);
                comb.remove(comb.size() - 1);
            }
        }
    }

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();
        backtracking(res, 0, target, candidates, new ArrayList<>(), 0);
        return res;
    }
}