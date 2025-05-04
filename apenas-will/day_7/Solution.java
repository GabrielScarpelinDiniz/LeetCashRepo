class Solution {
    public String reverseVowels(String s) {
        Set<Character> vowels = new HashSet<>();
        vowels.add('a');
        vowels.add('A');
        vowels.add('e');
        vowels.add('E');
        vowels.add('i');
        vowels.add('I');
        vowels.add('o');
        vowels.add('O');
        vowels.add('u');
        vowels.add('U');

        StringBuilder res = new StringBuilder(s);
        int lo = 0;
        int hi = s.length() - 1;
        
        while(lo < hi){
            if (vowels.contains(s.charAt(lo)) && vowels.contains(s.charAt(hi))){
                res.setCharAt(lo, s.charAt(hi));
                res.setCharAt(hi, s.charAt(lo));
                lo ++;
                hi --;
            }
            if (!vowels.contains(s.charAt(lo))){
                lo ++;
            }
            if(!vowels.contains(s.charAt(hi))){
                hi --;
            }
        }
        return res.toString();
    }
}