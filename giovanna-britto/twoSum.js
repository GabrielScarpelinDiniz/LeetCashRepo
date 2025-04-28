/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for (let i = 0; i < nums.length; i++){
        for (let j = i++; j < nums.length; j++){
            let sum = nums[i] + nums[j];
            if (sum === target){
                let indice = [i, j];
                return indice;
            }
        }
    }        
};