/**
 * @param {number} n
 * @return {boolean}
 */
var isUgly = function(n) {
    if (n < 1){
        return false
    }

    let arr = [2, 3, 5]

    for(let i = 0; i < arr.length; i++){
        while(n % arr[i] == 0){
            n = n / arr[i]
        }
    }

    return n == 1
};