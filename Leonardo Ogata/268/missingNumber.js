/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    let paSum = (nums.length / 2) * (2 * 1 + (nums.length - 1) * 1)
    let arrSum = 0

    for(let i = 0; i < nums.length; i++){
        arrSum += nums[i]
    }

    return paSum - arrSuma
};