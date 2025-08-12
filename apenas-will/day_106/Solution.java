class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> res = new ArrayList<>();

        for(int row = 0; row < numRows; row++){
            if(row == 0){
                res.add(Arrays.asList(1));
            } else {
                List<Integer> temp = new ArrayList<>();
                for(int element = 0; element < res.get(row - 1).size() + 1; element++){
                    if(element == 0){
                        temp.add(1);
                    } else if(element == res.get(row - 1).size()){
                        temp.add(1);
                    } else {
                        temp.add(res.get(row - 1).get(element) + res.get(row-1).get(element - 1));
                    }
                }
                res.add(temp);
            }
        }

        return res;
    }
}