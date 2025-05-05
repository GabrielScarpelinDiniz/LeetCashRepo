import java.util.ArrayList;

class Solution {
    public int removeElement(int[] nums, int val) {
        ArrayList<Integer> filteredList = new ArrayList<>();

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                filteredList.add(nums[i]);
            }
        }

        for (int i = 0; i < filteredList.size(); i++) {
            nums[i] = filteredList.get(i);
        }

        return filteredList.size();
    }
}