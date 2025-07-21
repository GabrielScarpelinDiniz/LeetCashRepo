class Solution {
    public int mySqrt(int x) {
        long lo = 0;
        long hi = x;
        long mid = (hi - lo) / 2;

        while(mid * mid != x){
            if(mid * mid > x){
                hi = mid;
                mid = (hi - lo) / 2;
            } else if (mid * mid < x){
                lo = mid + 1;
                mid = lo + ((hi - lo) / 2);
            }
            
            if(x > mid * mid && x < (mid + 1) * (mid + 1)){
                break;
            }
        } 

        return (int) mid;
    }
}