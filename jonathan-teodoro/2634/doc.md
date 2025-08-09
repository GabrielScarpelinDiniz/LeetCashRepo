/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
 var filter = function(arr, fn) {
    const filteredArr = [];
    for (let i = 0; i < arr.length; i++) {
        if (fn(arr[i], i)) {
            filteredArr.push(arr[i]);
        }
    }
    return filteredArr;
};

A função percorre o array verificando cada elemento com a função fn. Se o retorno for truthy, o elemento é adicionado a um novo array. No final, retorna apenas os elementos que passaram no filtro, sem usar Array.filter.