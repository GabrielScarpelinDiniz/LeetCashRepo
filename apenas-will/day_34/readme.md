## Exercício: 2331. Evaluate Boolean Binary Tree
**Objetivo**: Dada uma árvore binária que representa uma sequência de operações booleanas (as folhas da árvore são `1` ou `0`, os nós intermediários podem ser `2`, indicando a operação de `OR` ou `3` indicando a operação de `AND`), determine o resultado final da proposição;

## Descrição geral da estratégia
Para resolver, usei uma abordagem recursiva na qual determino o resultado das sub-árvores da esquerda e direita de forma recursiva, avaliando, por fim, o resultado da operação atual com base no valor da raiz.

## Análise de complexidade
Para uma árvore com $n$ nós, tem-se:
- **Time complexity**: $O(n)$
- **Space complexity**: $O(\log(n))$ (as árvores do exercício são sempre balanceadas) 