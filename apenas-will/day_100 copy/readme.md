## Exercício: 27. Remove Element
**Objetivo**: Dado um array de inteiros e um elemento, remova todos as aparições desse elemento do array in-place e retorne a quantidade de elementos restantes após a remoção.

## Descrição geral da estratégia
Para resolver uso dois ponteiros. Um primeiro avança uma posição a cada iteração de um loop e ele verifica se o elemento nessa posição é àquele que tem de ser eliminado. Se ele for, então o elemento na posição do outro ponteiro é substituído pelo elemento na posição do ponteiro que anda 1 a cada iteração e o ponteiro que ficou na posição é incrementado em 1. Esse processo continua até o final do array, sendo retornado, ao final, o valor do ponteiro mais lento.

## Análise de complexidade
Para um array com $n$ inteiros, tem-se:
- **Time complexity**: $O(n)$ 
- **Space complexity**: $O(1)$
