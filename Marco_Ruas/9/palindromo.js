/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let invertido = parseInt(x.toString().split('').reverse().join(''));

    if (invertido === x){
        return true
    }
    else{
        return false
    }
};