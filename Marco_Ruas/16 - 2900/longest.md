# Sprint do subsequente

## Desafio 16/200

Hoje o desafio foi daqueles: dado um array de palavras e um array de grupos (um grupo pra cada palavra), preciso montar a maior subsequência possível onde não pode repetir grupo seguido. Ou seja, se o grupo mudou, pode adicionar a palavra, se não, ignora e segue o baile.

Código:
Primeiro, já crio um array `result` pra guardar a resposta. Se não tem palavra, já devolvo vazio porque não tem o que fazer. Começo colocando a primeira palavra no resultado e salvo o grupo dela. Depois, vou varrendo o resto das palavras: se o grupo mudou em relação ao anterior, mando a palavra pro resultado e atualizo o grupo. Se for igual, ignoro e sigo.

No fim, devolvo o array com a maior subsequência possível sem grupos repetidos em sequência. Simples, direto e sem enrolação.

```javascript
/**
 * @param {string[]} words
 * @param {number[]} groups
 * @return {string[]}
 */
var getLongestSubsequence = function(words, groups) {

    const result = [];
    if (words.length === 0) return result;

    result.push(words[0]); 
    let lastGroup = groups[0];

    for (let i = 1; i < words.length; i++) {
        if (groups[i] !== lastGroup) {
            result.push(words[i]);
            lastGroup = groups[i];
        }
    }

    return result;
};
```



[Pizza](https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/submissions/1634246918)