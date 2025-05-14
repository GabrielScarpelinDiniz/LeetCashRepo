# Dia y de Leet Cash

Boa noite, Gente! Não tenho muito tempo (já é 23h46), então a documentação vai ser bem ruim. Eu resolvi o exercício 62, que também é de programação dinâmica, mas dessa vez com matrizes. Os passos do algoritmo consistem em:

1. Cria uma matriz dp com ``m`` linhas e ``n`` colunas, onde cada célula ``dp[i][j]`` representará quantos caminhos únicos existem até aquela posição.

2. Inicializa todas as células da primeira linha e da primeira coluna com o valor 1, pois só há uma maneira de chegar nelas: vindo da esquerda ou de cima, respectivamente.

3. A partir da célula (1,1), aplica a fórmula da Programação Dinâmica: `dp[i][j] = dp[i-1][j] + dp[i][j-1]`

4. Ao final, retorna ``dp[m-1][n-1]``, que contém o número de caminhos até o destino final.

Então é isso, problema resolvido, até a próxima!!