class Solution {
    public int singleNumber(int[] nums) {
        int b = 0;
        for(int i: nums){
            b ^= i;
        }

        return b;
    }
}