# Dia Z de LeetCash

Essa semana tem sido difícil, e especialmente hoje foi um dia muito ruim, o importante é se manter resiliente e não desistir em meio as dificuldades, por conta disso que eu estou aqui! Hoje eu resolvi o problema do caminho mínimo, no qual dado uma matriz você dizer qual o menor caminho para sair do canto esquerdo até o canto inferior direito, sendo que eu devo percorrer somente para a direita e para a baixo. 

Para resolver isso eu sigo os seguintes passos:

1. Defino as variáveis `m` e `n` como o número de linhas e colunas da grade, respectivamente.
2. Crio uma matriz `dp` de tamanho `m x n` para armazenar a soma mínima acumulada até cada célula.
3. Percorro a grade usando dois for, onde `i` representa as linhas e `j` representa as colunas.
4. Se a célula atual for a posição inicial `(0, 0)`, atribui a ela o valor correspondente da grade(ponto de partida).
5. Se estiver na primeira linha (`i == 0`), significa que só é possível vir da esquerda, então soma o valor atual da grade com o valor acumulado da célula à esquerda.
6. Se estiver na primeira coluna (`j == 0`), significa que só é possível vir de cima, então soma o valor atual da grade com o valor acumulado da célula acima.
7. Se nenhum dos casos acima, soma o valor atual da grade com o menor valor acumulado entre a célula de cima e a da esquerda.
8. Retorna o valor da última célula `dp[m-1][n-1]`

É isso gente, obrigada pela atenção de todos!!
