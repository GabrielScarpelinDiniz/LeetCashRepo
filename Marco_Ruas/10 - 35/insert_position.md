# Se eu não tivesse perdido minha ofensiva, estaria muito feliz

## Desafio 10/200

Hoje foi um dia atípico, tô cheio de coisa pra fazer mas tô com tempo vago, muito suspeito.

Dito isso consegui fazer esse exercício sem abdicar muito tempo. Basicamente ele vai dá uma lista e um alvo, aí você tem que dizer o índice desse alvo na lista, se o alvo não existe na lista e for menor que o índice próximo, retorna o índice do valor mais próximo, se não retorna o tamanho da lista.

O que o código faz:

1 - Ele percorre a lista (nums) com um loop.

2 - Verifica se o valor atual é igual ao target. Se for, retorna o índice.

3 - Caso contrário, verifica se o target é menor que o valor atual. Se for, retorna o índice onde o target deveria ser inserido.

4 - Se o loop terminar sem encontrar um índice apropriado, significa que o target é maior que todos os valores da lista, então retorna o tamanho da lista (nums.length).

```javascript
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === target) {
            return i;
        } else if (target < nums[i]) {
            return i;
        }
    }
    return nums.length;
};
```


[Au baby im prying you tonight ](https://leetcode.com/problems/search-insert-position/submissions/1628807529)