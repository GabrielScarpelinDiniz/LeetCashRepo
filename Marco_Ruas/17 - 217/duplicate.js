/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
  let repetir = {};

  for(let i = 0; i < nums.length; i++){
    if(repetir[nums[i]] === true){
        return true;
    }
    repetir[nums[i]] = true;
  }
  return false;
};