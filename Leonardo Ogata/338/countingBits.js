/**
 * @param {number} n
 * @return {number[]}
 */
var countBits = function(n) {
    arr = []
    for(let i = 0; i < n + 1; i++){
        dec = i
        binary = 0

        while (dec > 0) {
            binary = (dec % 2) + binary;
            dec = Math.floor(dec / 2);
        }

        arr.push(binary)
    }

    return arr

};
