/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let filtro = [];
    for (let i = 0; i<arr.length;i++){
        if(fn(arr[i], i)){
            filtro.push(arr[i]);
        }
    }
    return filtro
};