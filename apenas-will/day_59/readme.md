## Exercício: 112. Path Sum
**Objetivo**: Dada uma árvore binária, indique se há um caminho da raiz até alguma folha que a soma dos nós desse caminho resultam em um `target`;

## Descrição geral da estratégia
Para resolver uso um princípio do backtracking aplicando-o à um DFS. Nesse sentido, verifico recursivamente se a soma do valor de um nó com a sub-árvore da esquerda resulta no `target`, retornando `true` caso verdadeiro. Em seguida, tento o mesmo com a sub-árvore da direita, retornando `true` caso verdadeiro e `false` caso contrário.

## Análise de complexidade
Para um árvore com $n$ nós, tem-se:
- **Time complexity**: $O(n)$
- **Space complexity**: $O(\log(n))$