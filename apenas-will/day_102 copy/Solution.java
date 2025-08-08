class Solution {
    public void backtracking(List<List<Integer>> res, Map<Integer, Integer> candidates, int target, List<Integer> combination, int val){
        if(val == target){
            res.add(new ArrayList<>(combination));
        }

        for(int candidate: candidates.keySet()){
            if(candidates.get(candidate) > 0 && val + candidate <= target){
                if(combination.size() > 0){
                    if(candidate >= combination.get(combination.size() -1)){
                        candidates.compute(candidate, (k, v) -> v - 1);
                        val += candidate;
                        combination.add(candidate);
                        backtracking(res, candidates, target, combination, val);
                        candidates.compute(candidate, (k, v) -> v + 1);
                        val -= candidate;
                        combination.remove(combination.size() - 1);
                    }
                } else {
                    candidates.compute(candidate, (k, v) -> v - 1);
                    val += candidate;
                    combination.add(candidate);
                    backtracking(res, candidates, target, combination, val);
                    candidates.compute(candidate, (k, v) -> v + 1);
                    val -= candidate;
                    combination.remove(combination.size() - 1);
                }
            }
        }
    }
    
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();
        Map<Integer, Integer> counts = new HashMap<>();
        
        for(int i: candidates){
            counts.putIfAbsent(i, 0);
            counts.compute(i, (k, v) -> v + 1);
        }

        backtracking(res, counts, target, new ArrayList<>(), 0);
        
        return res;
    }
}