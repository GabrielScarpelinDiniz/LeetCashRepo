/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let remover = s.trim().split(' '); 
    return remover[remover.length - 1].length
}