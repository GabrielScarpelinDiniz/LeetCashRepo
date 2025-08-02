/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let result = init;
    for (let i = 0; i < nums.length; i++) {
        result = fn(result, nums[i]);
    }
    return result;
};

Implementei um reduce manual percorrendo o array nums com um loop. Começo com o valor inicial init, aplico a função fn acumulando o resultado a cada iteração e retorno o valor final. Se o array estiver vazio, retorna init. 
