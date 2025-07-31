## Exercício: 63. Unique Paths II
**Objetivo**: Dada uma matriz de inteiros na qual 0 indica um caminho livre e 1 indica um obstáculo, determine qual o o número de caminhos que um robô pode tomar para sair do canto superior esquerdo e chegar ao canto inferior direito evitando os obstáculos.

## Descrição geral da estratégia
Para resolver utilizo uma abordagem de programação dinâmica que vai progressivamente salvando a quantidade de caminhos possíveis do canto superior esquerdo até uma determinada posição. Nesse contexto, crio a matriz `uniquePathsTo`, na qual `uniquePathsTo[i][j]` indica quantos caminhos existem entre o canto superior esquerdo e a casa na linha `i` e coluna `j`. Para isso, percorro a matriz, indicando que a quantidade de caminhos até determinada posição é igual a soma de caminhos que chegam à casa acima e à esquerda da casa em questão. Para lidar com os obstáculos, basta considerar que eles são posições na quais não há caminhos que possam chegar até eles e, portanto, são salvos como 0. Um ponto de atenção são os obstáculos na primeira linha e coluna, pois, a partir deles, tudo fica zerado. Sendo assim, basta, depois que encontrá-los em alguma posição nessa linha ou coluna, zerar todo o resto. Repito os processos anteriores até o final da matriz e retorno o valor presente na última posição.

## Análise de complexidade
Para uma matriz com $m$ linhas e $n$ colunas, tem-se:
- **Time complexity**: $O(m \times n)$ 
- **Space complexity**: $O(m \times n)$
