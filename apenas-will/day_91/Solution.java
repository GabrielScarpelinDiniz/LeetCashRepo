class Solution {
    public String countAndSay(int n) {
        String[] res = new String[n];
        res[0] = "1";
        for(int i = 1; i < n; i++){
            int lo = 0;
            int hi = 0;
            StringBuilder temp = new StringBuilder();
            while(hi < res[i - 1].length()){
                if(res[i-1].charAt(lo) != res[i-1].charAt(hi)){
                    temp.append(hi - lo);
                    temp.append(res[i-1].charAt(lo));
                    lo = hi;
                }
                hi++;
            }
            temp.append(hi - lo);
            temp.append(res[i-1].charAt(lo));
            res[i] = temp.toString();
        }
        
        return res[n - 1];
    }
}