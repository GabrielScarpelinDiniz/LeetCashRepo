var majorityElement = function(nums) {
    let valor = {};
    let limite = Math.floor(nums.length / 2);

    for(let i = 0; i < nums.length; i++){
        valor[nums[i]] = (valor[nums[i]] || 0) + 1;

        if (valor[nums[i]] > limite) {
            return nums[i];
        }
    }
};
