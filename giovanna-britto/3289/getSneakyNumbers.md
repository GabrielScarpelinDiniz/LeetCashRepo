# Mais um dia de LeetCash

Boa noite Gente!! Hoje eu resolvi mais o exercício 3289, no qual eu precisava encontrar dois números furtivos em uma lista que deveria conter números de `0` até `n-1`, mas com dois números aparecendo uma vez a mais. Para resolver isso eu segui os seguintes passos:

1. Utilizei o `Counter` da biblioteca  para contar quantas vezes cada número aparece na lista `nums`.
2. Criei a lista `furtivos`, que:

   * Percorre os pares `(num, freq)` do dicionário de contagem
   * Verifica se `freq == 2`, ou seja, se o número apareceu duas vezes
   * Adiciona o número à lista `furtivos`

3. Retorno final da lista `furtivos`, que contém exatamente os dois números duplicados.

Pronto! Mais um exercício resolvido!!!