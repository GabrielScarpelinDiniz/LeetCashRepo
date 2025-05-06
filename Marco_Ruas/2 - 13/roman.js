/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    var numero = 0;
    var valores = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    };

    for (var i = 0; i < s.length; i++) {
        var atual = valores[s[i]];
        var proximo = valores[s[i + 1]];

        if (proximo > atual) {
            numero -= atual;
        } else {
            numero += atual;
        }
    }

    return numero;
};

console.log(romanToInt("XIV")); 
console.log(romanToInt("MCMXCIV")); 