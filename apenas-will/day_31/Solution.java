class Solution {
    public int hammingDistance(int x, int y) {
        String q = Integer.toBinaryString(x ^ y);
        int res = 0;
        
        for(int i = 0; i < q.length(); i ++){
            if(q.charAt(i) == '1'){
                res++;
            }
        }
        return res;
    }
}