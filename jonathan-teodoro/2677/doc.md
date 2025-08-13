A função percorre o array em saltos de size e usa slice para criar subarrays de tamanho fixo. Caso a quantidade de elementos não seja múltipla de size, o último subarray terá menos elementos.

/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    let result = [];
    for (let i = 0; i < arr.length; i += size) {
        result.push(arr.slice(i, i + size));
    }
    return result;
};

