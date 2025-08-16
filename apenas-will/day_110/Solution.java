class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        if(n == 0) return true;
        if(flowerbed.length == 1){
            if(flowerbed[0] == 1) return false;
            return true;
        }
        int placed = 0;
        for(int i = 0; i < flowerbed.length; i++){
            if(flowerbed[i] == 0){
                if(i > 0 && i < flowerbed.length - 1){
                    if(flowerbed[i - 1] == 0 && flowerbed[i + 1] == 0){
                        flowerbed[i] = 1;
                        placed ++;
                    }
                } else if (i == 0){
                    if(flowerbed[1] == 0){
                        flowerbed[i] = 1;
                        placed ++;
                    }
                } else {
                    if(flowerbed[i - 1] == 0){
                        flowerbed[i] = 1;
                        placed ++;
                    }
                }
            }
            if(placed == n) return true; 
        }

        return placed >= n;
    }
}