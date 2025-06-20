## Exercício: 398. Random Pick Index
**Objetivo**: Dada uma lista de inteiros com duplicatas, crie uma classe que, dado um `target` retorne de forma equiprovável um possível índice para esse elemento;

## Descrição geral da estratégia
Para resolver, primeiro armazeno a lista de elementos como um `HashMap`, no qual as chaves são os inteiros e os valores são listas contendo todos os índices que aqueles valores aparecem. Em seguida, dado um `target`, sorteio um índice que esteja no intervalo de 0 ao tamanho da lista de indices para esse valor, retornando por fim o elemento que está naquele índice (isto é, um índice aleatório do `target`).

## Análise de complexidade
Para um array com $n$ inteiros, tem-se:
- **Time complexity**: 
    - Armazenamento da entrada: $O(n)$
    - Geração de resultado: $O(1)$
- **Space complexity**: $O(n)$