class Solution {
    public int lengthOfLastWord(String s) {
        int max = 0;
        
        for(int i = s.length() - 1 ; i > -1; i--){
            if(max != 0 && s.charAt(i) == ' '){
                break;
            } else if (s.charAt(i) != ' '){
                max ++;
            } 
        }

        return max;
    }
}