class Solution {
    public void backtrack(List<String> res, StringBuilder s, int i){
        if(i == s.length()){
            res.add(s.toString());
            return;
        }

        if(Character.isLetter(s.charAt(i))) {
            s.setCharAt(i, Character.toLowerCase(s.charAt(i)));
            backtrack(res, s, i + 1);
        
            s.setCharAt(i, Character.toUpperCase(s.charAt(i)));
            backtrack(res, s, i + 1);
        } else {
            backtrack(res, s, i + 1);
        }
    }

    public List<String> letterCasePermutation(String s) {
        List<String> res = new ArrayList<>();

        backtrack(res, new StringBuilder(s), 0);

        return res;
    }
}