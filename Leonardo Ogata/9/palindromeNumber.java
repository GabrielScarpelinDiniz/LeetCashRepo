class Solution {
    public boolean isPalindrome(int x) {
        int origin = x;
        int resverse = 0;
        
        while (x > 0) {
            int rest = x % 10;
            resverse = resverse * 10 + rest;
            x = x / 10;
        }

        if (origin == resverse) {
            System.out.println("Palindromo");
            return true;
        }else{
            System.out.println("Nem é");
            return false;
        }
    }
}