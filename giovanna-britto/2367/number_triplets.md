# Mais um dia de LeetCash

Hoje eu resolvi o exercício 2367, que pede para contar quantos trios (i, j, k) existem em um array, com i < j < k, formando uma progressão aritmética com uma diferença (`diff`). Para isso eu segui os seguintes passos:

1. Criei uma variável `cont` para contar os trios válidos.
2. Usei três fors para passar por todas as combinações possíveis de índices i, j, k, garantindo que i < j < k.
3. Para cada trio, verifiquei se `nums[k] - nums[j] == diff` e `nums[j] - nums[i] == diff`.
4. Se as duas condições forem verdadeiras, aumentei `cont` em 1.
5. No final, retornei `cont` com o total de trios encontrados.

E pronto! Mais um exercício resolvido!!!