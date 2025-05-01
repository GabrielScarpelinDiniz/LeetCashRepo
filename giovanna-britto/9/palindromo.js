/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if (x < 0) return false;

    let newWord = '';
    x = x.toString();

    for (let i = x.length-1; i >= 0; i--){
        newWord += x[i];
    }

    if (newWord == x){
        return true;
    } else {
        return false;
    }
};