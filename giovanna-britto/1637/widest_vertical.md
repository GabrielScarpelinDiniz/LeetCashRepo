# Mais um dia de LeetCash

Hoje eu resolvi o exercício 1637, que pede para encontrar a maior largura de uma área vertical entre pontos em um plano 2D. A largura é a maior diferença entre as coordenadas x de pontos consecutivos, depois de ordenar todos os pontos pelo x. Resolvi assim:

1. Ordenei a lista `points` pelo valor x de cada ponto.

2. Criei uma variável `diferenca` para guardar a maior diferença encontrada.

3. Usei um for para passar por todos os pontos a partir do segundo:

    3.1. Para cada ponto, calculei a diferença entre o x atual e o x anterior.

    3.2. Atualizei `diferenca` se a diferença for maior que o valor anterior.

4. No final, retornei `diferenca` como resposta.

Pronto! Exercício resolvido. Boa noite pessoal, até a próxima!!!