/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    let result = [];
    for (let i = 0; i < arr.length; i++) {
        result.push(fn(arr[i], i));
    }
    return result;
};

A função percorre o array original e aplica a função fn a cada elemento junto com seu índice, armazenando os resultados num novo array. É basicamente uma implementação manual do Array.map, garantindo que não se use o método embutido.