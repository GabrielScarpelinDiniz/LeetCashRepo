class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        Map<Character, Integer> sMap = new HashMap<>();
        Map<Character, Integer> tMap = new HashMap<>();
        
        for(int i = 0; i < s.length(); i++){
            int sCount = sMap.containsKey(s.charAt(i))? sMap.get(s.charAt(i)) : 0;
            int tCount = tMap.containsKey(t.charAt(i))? tMap.get(t.charAt(i)) : 0;

            sMap.put(s.charAt(i), sCount + 1);
            tMap.put(t.charAt(i), tCount + 1);
        }

        if(sMap.size() != tMap.size()) {
            return false;
        }
        
        for(Character c: sMap.keySet()){
            if(!tMap.containsKey(c)) {
                return false;
            }
            if(sMap.get(c)/2 != tMap.get(c)/2){
                return false;
            }
        }

        return true;
    }
}