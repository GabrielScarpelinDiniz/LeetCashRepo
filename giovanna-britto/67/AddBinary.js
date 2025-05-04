
/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {

    let i = a.length-1;
    let j = b.length-1;
    let aux = 0;
    let resultado = [];

    while (i >= 0 || j >= 0 || aux != 0){
        if (i >= 0){
            var valorA = parseInt(a[i]);
        } else {
            valorA = 0;
        }

        if (j >= 0){
            var valorB = parseInt(b[j])
        } else {
            valorB = 0;
        }

        let soma = valorA + valorB + aux;
        aux = Math.floor(soma / 2);
        resultado.push(soma % 2);

        i--;
        j--;
    }

    return resultado.reverse().join('');
};