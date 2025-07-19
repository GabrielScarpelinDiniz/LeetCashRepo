# Mais um dia de LeetCash

Hoje eu resolvi o exercício 2220, que pede para calcular o número mínimo de flips de bits para transformar um número `start` em `goal`. Para isso eu segui os seguintes passos:

1. Calculei o XOR entre `start` e `goal`, guardando o resultado em `resultado`. Assim, cada bit diferente entre os dois vira 1.

2. Criei uma variável `resposta` para contar quantos bits precisam ser flipados.

3. Usei um while para percorrer todos os bits de `resultado`:

    3.1. Somei 1 em `resposta` se o último bit for 1 (`resultado & 1`).

    3.2. Desloquei `resultado` para a direita para checar o próximo bit.

4. No final, retornei `resposta` com o total de flips necessários.

E pronto! Mais um exercício resolvido!!