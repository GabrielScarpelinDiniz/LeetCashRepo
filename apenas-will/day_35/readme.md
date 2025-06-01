## Exercício: 2133. Check if Every Row and Column Contains All Numbers
**Objetivo**: Dada uma uma matriz de inteiros, determine se todas as linhas e colunas contém todos os inteiros de 1 ao tamanho da linha/coluna (para uma matrix 3 x 3, todas as linhas e colunas devem conter 1, 2 e 3);

## Descrição geral da estratégia
Para resolver, itero pelas linhas adicionando os elementos em um `HashSet`, ao final, confiro se o comprimento do conjunto é igual ao comprimento da linha/coluna (`Set` nunca contém elementos duplicados).

## Análise de complexidade
Para uma matrix $n \times n$, tem-se:
- **Time complexity**: $O(n^2)$
- **Space complexity**: $O(n)$ 