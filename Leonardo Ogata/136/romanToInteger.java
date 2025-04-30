import java.util.HashMap;

class Solution {
    public int romanToInt(String s) {
        HashMap<Character, Integer> romanNumeral = new HashMap<>();
        romanNumeral.put('I', 1);
        romanNumeral.put('V', 5);
        romanNumeral.put('X', 10);
        romanNumeral.put('L', 50);
        romanNumeral.put('C', 100);
        romanNumeral.put('D', 500);
        romanNumeral.put('M', 1000);
        
        int inteiro = 0;

        for (int i = 0; i < s.length(); i++) {
            if (i + 1 < s.length() && romanNumeral.get(s.charAt(i)) < romanNumeral.get(s.charAt(i + 1))) {
                inteiro += romanNumeral.get(s.charAt(i + 1)) - romanNumeral.get(s.charAt(i));

                i++;

            }else{

                inteiro += romanNumeral.get(s.charAt(i));
            }
            
        }

        return inteiro;
    }
}