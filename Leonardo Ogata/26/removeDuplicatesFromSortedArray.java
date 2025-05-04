import java.util.ArrayList;

class Solution {
    public int removeDuplicates(int[] nums) {
        ArrayList<Integer> correct = new ArrayList<>();

        int atual = 0;

        for (int i = 0; i < nums.length; i++){
            if (i == 0) {
                atual = nums[i];
                correct.add(nums[i]);
            }

            if (nums[i] != atual) {
                atual = nums[i];
                correct.add(nums[i]);
            }
        }

        for (int i = 0; i < correct.size(); i ++) {
            nums[i] = correct.get(i);
        }
        
        return correct.size();
    }
}