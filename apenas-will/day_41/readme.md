## Exercício: 257. Binary Tree Paths
**Objetivo**: Dada uma árvore binária, diga todos os caminhos que ligam a raiz às folhas;

## Descrição geral da estratégia
Para resolver implementei um algoritmo de backtracking que cria o caminho de maneira recursiva (adicionando nó a nó) e, quando chega em uma folha, adiciona esse caminho num array com as soluções. 

## Análise de complexidade
Para uma árvore com $n$ nós, tem-se:
- **Time complexity**: $O(n)$ 
- **Space complexity**: $O(n)$ ( $O(\log(n))$ para árvores balanceadas)