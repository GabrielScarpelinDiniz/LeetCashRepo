class Solution {
    /**
     * @param Integer $n
     * @return Boolean
     */
    function isPowerOfFour($n) {
        if ($n == 1){
            return true;
        }else if($n < 1){
            return false;
        }

        return $this->isPowerOfFour($n / 4);
    }
}