class Solution {
    public boolean judgeCircle(String moves) {
        int[] counts = new int[4];
        for(int i = 0; i < moves.length(); i++){
            if (moves.charAt(i) == 'U'){
                counts[0] ++;
            }
            if (moves.charAt(i) == 'D'){
                counts[1] ++;
            }
            if (moves.charAt(i) == 'L'){
                counts[2] ++;
            }
            if (moves.charAt(i) == 'R'){
                counts[3] ++;
            }
        }

        return counts[0] - counts[1] == 0 && counts[2] - counts[3] == 0;
    }
}