class Solution {
    public int eval(int a, int b, int x){
        if((Math.abs(a - x) < Math.abs(b - x)) || ((Math.abs(a - x) == Math.abs(b - x)) && a < b)){
            return 1;
        }
        return -1;
        
    }

    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        PriorityQueue<Integer> res = new PriorityQueue<>((a, b) -> eval(a, b, x));
        for(int i: arr){
            res.add(i);
            if(res.size() > k){
                res.remove();
            }
        }
        
        List<Integer> ans = new ArrayList<>();

        while(!res.isEmpty()){
            ans.add(res.remove());
        }
        
        Collections.sort(ans);

        return ans;
    }
}