# Mais um dia de LeetCash

Hoje resolvi o exercício 1486, que pede para calcular o XOR de uma sequência onde cada elemento é `start + 2*i` para `i` de 0 até `n-1`. Resolvi assim:

1. Criei uma variável `primeiro` que começa com o valor de `start`.
2. Usei um for de 1 até `n-1` para calcular os próximos elementos da sequência.
3. Em cada passo, fiz o XOR de `primeiro` com o valor `start + 2*i`.
4. No final, retornei o valor de `primeiro`, que é o resultado do XOR de toda a sequência.

E pronto! Mais um exercício resolvido!!!