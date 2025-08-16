class Solution {
    public String reverseWords(String s) {
        StringBuilder res = new StringBuilder();
        int lo = 0;
        
        StringBuilder temp = new StringBuilder();
        for(int hi = 0; hi < s.length(); hi ++){
            if(s.charAt(hi) == ' ' && s.charAt(lo) != ' '){
                res.append(temp.reverse());
                res.append(' ');
                temp.setLength(0);
                lo = hi + 1;
            } else if(s.charAt(hi) != ' '){
                temp.append(s.charAt(hi));
            }
        }
        res.append(temp.reverse());

        return res.toString();
    }
}