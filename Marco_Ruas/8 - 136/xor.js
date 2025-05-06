/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    let repetido = 0;
    for(let i = 0; i < nums.length; i++){
        repetido = repetido ^ nums[i]
    }
    return repetido
};