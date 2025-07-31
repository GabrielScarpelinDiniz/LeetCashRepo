## Exercício: 62. Unique Paths
**Objetivo**: Dado dos inteiros $m$ e $n$ qu representam o número de linhas e colunas de um tabuleiro que um robô terá de percorrer, determine qual o número de caminhos únicos que esse robô pode tomar para sair do canto superior esquerdo e chegar ao canto inferior direito (considere que o robô só pode andar para a direita e para baixo).

## Descrição geral da estratégia
Para resolver utilizo uma abordagem de programação dinâmica que vai progressivamente salvando a quantidade de caminhos possíveis do canto superior esquerdo até uma determinada posição. Nesse contexto, crio a matriz `numPaths`, na qual `numPaths[i][j]` indica quantos caminhos existem entre o canto superior esquerdo e a casa na linha `i` e coluna `j`. Para isso, percorro a matriz, indicando que a quantidade de caminhos até determinada posição é igual a soma de caminhos que chegam à casa acima e à esquerda da casa em questão. Como ponto de partida, supõe-se que para chegara qualquer casa na primeira linha é necessário apenas ir para a direita, forçando que só haja 1 caminho para qualquer uma dessas casas. O mesmo se aplica para a primeira coluna, na qual, só se pode acessar partindo da posição inicial e indo para baixo. As quantidade de caminhos para as demais casas, como indicado anteriormente, é igual a soma da quantidade de caminhos na casa acima e à esquerda. Com isso, preencho a matriz conforme indicado até chegar ao ponto inferior esquerdo, retornando, por fim, a quantidade de caminhos presente no canto inferior direito.

## Análise de complexidade
Para uma matriz com $m$ linhas e $n$ colunas, tem-se:
- **Time complexity**: $O(m \times n)$ 
- **Space complexity**: $O(m \times n)$
