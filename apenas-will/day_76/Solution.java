class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int[] res = new int[k];
        Map<Integer, Integer> counts = new HashMap<>();

        for(int i: nums){
            counts.putIfAbsent(i, 0);
            counts.compute(i, (key, v) -> v + 1);
        }

        PriorityQueue<Integer> frequencyOrder = new PriorityQueue<>((a, b) -> counts.get(b) - counts.get(a)); // if a < b, the order will be a, b. If b < a, the order will be b, a

        for(int i: counts.keySet()){
            frequencyOrder.add(i);
        }

        for(int i = 0; i < k; i ++){
            if(!frequencyOrder.isEmpty()){
                res[i] = frequencyOrder.remove();
            }
        }

        return res;
    }
}