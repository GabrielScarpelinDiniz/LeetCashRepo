class Solution {
    public int maxArea(int[] height) {
        int temp = 0;
        int max = temp;
        int lo = 0;
        int hi = height.length - 1;

        while(lo != hi){
            temp = (hi - lo) * Math.min(height[lo], height[hi]);
            if(temp > max) max = temp;

            if(height[lo] < height[hi]) lo++;
            else hi--;
        }

        return max;
    }
}