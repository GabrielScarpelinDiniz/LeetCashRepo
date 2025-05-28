## Exercício: 111. Minimum Depth of Binary Tree
**Objetivo**: Dada um árvore, indique qual é a distância entre a raiz e a folha mais próxima (menor profundidade);

## Descrição geral da estratégia
Para resolver implementei um DFS recursivo que compara a menor altura da subárvore da esquerda e da direita, retornado a menor. Por fim, retorno esse valor.

## Análise de complexidade
Para uma árvore com $n$ nós, tem-se:
- **Time complexity**: $O(n)$
- **Space complexity**: $O(\log(n))$ 