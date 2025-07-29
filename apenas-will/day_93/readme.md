## Exercício: 64. Minimum Path Sum
**Objetivo**: Dado uma matriz de inteiros, indique o valor do menor caminho que conecte o elemento do canto superior esquerdo ao canto inferior direito. Um caminho é válido ao conectar elementos adjacentes, seja vertical ou horizontalmente (mas não nas diagonais) e o valor desse caminho é dado pelo valor presente nessa posição da matriz. Só se pode, dada uma posição, ir para a direita dessa posição ou para baixo.

## Descrição geral da estratégia
Para resolver utilizo uma abordagem de programação dinâmica que vai progressivamente salvando o menor caminho para se chegar a cada posição na matriz. Para isso, crio uma matrix auxiliar `sum`, na qual `sum[i][j]` indica o menor caminho saindo do canto superior esquerdo até a linha `i` e coluna `j`. Saindo do ponto $(0,0)$, o algoritmo vai explorar todas as linhas e colunas, determinando o menor caminho necessário para se chegar até essa posição baseado no valor que está acima ou à esquerda dele na matriz `sum`. Isso ocorre pois, como mencionado anteriormente, só se pode "andar" para a direita ou para baixo. Sendo assim, para se chegar à um ponto $(i,j)$ necessariamente o anterior foi $(i - 1, j)$ ou $(i, j - 1)$. Partindo desse principio e de que a matriz `sum` sempre armazena o menor caminho até determinada posição, basta selecionar o menor caminho entre as possibilidades anteriores, somar ao valor do posição atual e repetir esse processo até o final da matriz. Por fim, retorna-se o elemento presente no canto inferior direito da matriz `sum`, que armazena o menor caminho até tal posição.

## Análise de complexidade
Para uma matriz com $n$ linhas e $m$ colunas, tem-se:
- **Time complexity**: $O(n \times m)$ 
- **Space complexity**: $O(n \times m)$
