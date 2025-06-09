/**
 * @param {number[]} nums
 * @return {string[]}
 */
var summaryRanges = function(nums) {
    var start = 0
    var end = 0
    arr = []

    for(let i = 0; i < nums.length; i++){
        if(nums[i] + 1 == nums[i + 1]){
            end ++;
        }else{
            if(start == end){
                arr.push("" +  nums[start] + "")
                start = end + 1;
                end ++;
            }else{
                arr.push(nums[start] + "->" + nums[end])
                start = end + 1;
                end ++;
            }
        }
    }

    return arr

};