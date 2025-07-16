class Solution {
    public int thirdMax(int[] nums) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>(3);
        Set<Integer> visited = new HashSet<>();
        
        for(int i: nums){
            if(!visited.contains(i)) minHeap.add(i);
            visited.add(i);

            if(minHeap.size() > 3){
                minHeap.remove();
            }
        }   

        if(visited.size() < 3){
            int res = 0;

            for(int k : minHeap){
                res = k;
            }

            return res;
        }

        return minHeap.remove();
    }
}