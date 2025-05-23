/**
 * @param {string} s
 * @return {number}
 */
var scoreOfString = function(s) {
    let pontuacao = 0;

    for (let i = 0; i < s.length - 1; i++) {
        const valorAtual = s.charCodeAt(i);
        const valorProximo = s.charCodeAt(i + 1);
        pontuacao += Math.abs(valorAtual - valorProximo);
    }

    return pontuacao;  
};