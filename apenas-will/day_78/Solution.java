class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>(k);

        for(int i: nums){
            minHeap.add(i);
            if(minHeap.size() > k){
                minHeap.poll();
            }
        }

        return minHeap.remove();
    }
}