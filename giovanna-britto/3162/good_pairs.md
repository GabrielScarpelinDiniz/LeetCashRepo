# Mais um dia de LeetCash

Hoje eu resolvi o exercício 3162, que pede para contar quantos pares (i, j) existem entre dois arrays, onde o elemento de `nums1` é divisível por `j*k`, sendo `j` de `nums2` e `k` um inteiro dado. Para isso eu segui os seguintes passos:

1. Criei uma variável `cont` para contar os pares válidos.
2. Usei dois fors para passar por cada elemento de `nums1` e `nums2`.

    2.1. Para cada par, verifiquei se `i % (j*k) == 0`.

    2.2. Se for verdade, aumento `cont`.

3. No final, retornei `cont` com o total de pares encontrados.

E pronto! Mais um exercício resolvido!!