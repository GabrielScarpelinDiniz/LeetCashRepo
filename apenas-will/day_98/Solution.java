class Solution {
    public void backtracking(List<List<Integer>> res, int[] nums, List<Integer> perm, Map<Integer, Integer> counts){
        if(perm.size() == nums.length){
            res.add(new ArrayList<>(perm));
            return;
        }

        for(int element : counts.keySet()){
            if(counts.get(element) > 0){
                counts.compute(element, (k, v) -> v - 1);
                perm.add(element);
                backtracking(res, nums, perm, counts);
                perm.remove(perm.size() - 1);
                counts.compute(element, (k, v) -> v + 1);
            }
        }
    }
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Map<Integer, Integer> counts = new HashMap<>();

        for(int n : nums){
            counts.putIfAbsent(n, 0);
            counts.compute(n, (k, v) -> v + 1);
        }
        backtracking(res, nums, new ArrayList<>(), counts);

        return res;
    }
}