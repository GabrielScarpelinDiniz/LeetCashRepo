## Exercício: 107. Binary Tree Level Order Traversal II
**Objetivo**: Dada uma árvore binária, retorne uma lista de listas de cada nível da árvore (cada lista corresponde a um nível) ordenada das folhas a raiz;

## Descrição geral da estratégia
Para resolver aplico um BFS usando fila. Primeiramente, crio uma lista de resultados e a fila para o BFS. adiciono na fila a raiz e um nó `sep` que indica o final de um nível da árvore. A cada iteração, enquanto a fila não estiver vazia, adiciono os filhos do nó que estou analisando à última lista na lista de resultados. Caso eu encontre o separador, significa que o próximo nó pertence a um novo nível da árvore, então crio uma nova lista e adiciono o novo separador ao final da fila. Repito até ter passado por toda a árvore e retorno a lista de resultado de trás para frente.

## Análise de complexidade
Para uma árvore com $n$ nós e $l$ níveis, tem-se:
- **Time complexity**: $O(n + l)$
- **Space complexity**: $O(n + l)$