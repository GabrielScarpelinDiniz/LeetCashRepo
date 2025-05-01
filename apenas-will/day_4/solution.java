class Solution {
    public boolean isPalindrome(int x) {
        String num = Integer.toString(x);

        for(int i = 0; i < num.length(); i++){
            if(num.charAt(i) != num.charAt(num.length() - 1 - i)){
                return false;
            }
        }

        return true;
    }
}