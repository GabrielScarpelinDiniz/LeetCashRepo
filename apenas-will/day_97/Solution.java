class Solution {
    public String longestCommonPrefix(String[] strs) {
        if(strs.length == 1) return strs[0];

        StringBuilder res = new StringBuilder();
        for(int i = 0; i < strs[0].length(); i++){
            char current = strs[0].charAt(i);

            for(String str: strs){
                if(str.length() == 0) return "";
                if(str.length() <= i) return res.toString();
                if(str.charAt(i) != current) return res.toString();
            }
            res.append(current);
        }

        return res.toString();
    }
}