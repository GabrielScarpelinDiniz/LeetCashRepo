class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] prevProd = new int[nums.length];
        int[] posProd = new int[nums.length];

        prevProd[0] = 1;
        for(int i = 0; i < nums.length; i++){
            if(i > 0){
                prevProd[i] = prevProd[i - 1] * nums[i - 1];
            }
        }

        posProd[nums.length - 1] = 1;
        for(int i = nums.length - 1; i > -1; i--){
            if(i < nums.length - 1){
                posProd[i] = posProd[i + 1] * nums[i + 1];
            }
        }

        int[] res = new int[nums.length];

        for(int i  = 0; i < nums.length; i++){
            res[i] = prevProd[i] * posProd[i];
        }

        return res;
    }
}