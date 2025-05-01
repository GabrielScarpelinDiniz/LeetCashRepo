/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    const valorRomano = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    let total = 0;
    let bau = 0;

    for (let i = s.length - 1; i >= 0; i--){
        let atual = valorRomano[s[i]];

        if(atual < bau){
            total -= atual;
        } else {
            total += atual;
        }

        bau = atual;
    }

    return total;
};