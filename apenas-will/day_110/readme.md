## Exercício: 605. Can Place Flowers
**Objetivo**: Dado um array que representa um vaso de flores e um inteiro $n$, indique se é possível plantar $n$ flores no vaso. Para que uma flor seja plantada, é necessário que não haja flores adjacentes à ela.

## Descrição geral da estratégia
Para resolver uso uma abordagem gulosa que vai adicionando flores no vaso sempre que encontra-se um local adequado. Todas as vezes que uma flor é adicionada, incrementa-se uma variável auxiliar que armazena quantas flores já foram plantadas. Ao final, retorna-se o resultado booleano de uma expressão que confere se a quantidade de flores plantadas é maior ou igual ao valor $n$

## Análise de complexidade
Para um array com $m$ espaços, tem-se:
- **Time complexity**: $O(m)$
- **Space complexity**: $O(1)$
