class Solution {
    public void backtracking(List<List<Integer>> res, List<Integer> sol, Set<Integer> elem, int solSize, int[] poss, int k, int prox){
        if(solSize == k){
            res.add(new ArrayList<>(sol));
            return;
        }

        for(int i = prox; i < poss.length; i++){
            if(!elem.contains(poss[i])){
                elem.add(poss[i]);
                sol.add(poss[i]);
                backtracking(res, sol, elem, solSize + 1, poss, k, i);
                elem.remove(poss[i]);
                sol.remove(sol.size() - 1);
            }
        }
    }
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> sol = new ArrayList<>();
        Set<Integer> elem = new HashSet<>();
        int[] poss = new int[n];

        for(int i = 0; i < n; i++){
            poss[i] = i + 1;
        }

        backtracking(res, sol, elem, 0, poss, k, 0);
        return res;
    }
}