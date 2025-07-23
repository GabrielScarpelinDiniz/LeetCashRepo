# Mais um dia de LeetCash

Hoje eu resolvi o exercício 2824, que pede para contar quantos pares de índices (i, j) existem em um array onde i < j e a soma deles seja menor que um valor alvo (`target`). Para isso eu segui os seguintes passos:

1. Criei uma variável `res` para contar os pares válidos.

2. Usei dois fors para passar por todas as combinações possíveis de índices i e j, com j sempre maior que i.

3. Para cada par, verifiquei se a soma `numsi] + numsj]` é menor que `target`.

4. Se for, aumentei `res` em 1.

5. No final, retornei `res` com o total de pares encontrados.

E pronto! Mais um exercício resolvido!!!