class Solution {
    public int mySqrt(int x) {
        int temp = 0;

        while (true) {
            if((long)temp * temp > x){
                return temp - 1;
            }

            temp++;
        }

    }
}