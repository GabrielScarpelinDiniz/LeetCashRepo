# Sem tempo de novo

## Desafio 23/200

Não tenho tempo desculpa

### Reformulado no chatgpt

O código define uma função chamada scoreOfString que calcula a pontuação de uma string somando as diferenças absolutas entre os valores ASCII de caracteres adjacentes. Ele percorre a string do primeiro até o penúltimo caractere, usando charCodeAt(i) para obter o valor ASCII de cada caractere e de seu próximo, e depois usa Math.abs(...) para calcular a diferença absoluta entre esses dois valores. Cada diferença é acumulada em uma variável chamada pontuacao, que é retornada ao final. Dessa forma, a função retorna um número que representa o quanto os caracteres consecutivos da string diferem entre si em termos de seus códigos ASCII.

```javascript
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
```


[Remada](https://leetcode.com/problems/score-of-a-string/submissions/1640821389)