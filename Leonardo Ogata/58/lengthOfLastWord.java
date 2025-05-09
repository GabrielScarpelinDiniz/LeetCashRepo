class Solution {
    public int lengthOfLastWord(String s) {
        String regex = "[\\s]";

        String[] stringarray = s.split(regex);

        
        for(String a : stringarray){
            System.out.println(a);
        }

        return stringarray[stringarray.length - 1].length();
    }
}