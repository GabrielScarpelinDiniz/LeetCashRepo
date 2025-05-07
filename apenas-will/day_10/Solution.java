class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> conjunto = new HashSet<>();

        for(int i: nums){
            if(conjunto.contains(i)){
                return true;
            } else {
                conjunto.add(i);
            }
        } 

        return false;
    }
}