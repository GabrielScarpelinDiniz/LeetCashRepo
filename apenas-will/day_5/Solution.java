class Solution {
    public int missingNumber(int[] nums) {
        int expected = 0;
        int real = 0;
        for(int i = 0; i < nums.length; i++){
            expected += i;
            real += nums[i];
        }
        expected += nums.length;

        return expected - real;
    }
}