/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {

    let resultado = [nums[0]]

    for(let i = 1; i < nums.length; i++){
        resultado[i] = resultado[i-1] + nums[i];
    }  

    return resultado
} ;