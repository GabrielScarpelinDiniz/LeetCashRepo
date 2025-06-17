# Passando do dia 50 de Leetcash

Hoje resolvi o exercício 279, que pede para encontrar o menor número de quadrados perfeitos cuja soma seja igual a n. Resolvi usando recursão com memoização. Para isso eu segui os seguintes passos:

1. Criei uma lista `memo` para guardar os resultados já calculados e evitar repetir contas.
2. Se n for 0, retorno 0 (caso base).
3. Se n for menor que 0, retorno infinito (não é possível).
4. Se já calculei o resultado para esse n, retorno o valor salvo em `memo`.
5. Defini uma variável `mini` para guardar o menor número de quadrados perfeitos.
6. Usei um while para testar todos os quadrados perfeitos menores ou iguais a n:

    6.1. Para cada quadrado perfeito, faço a chamada recursiva para `n - (i*i)` e atualizo o mínimo.

7. Salvo o resultado em `memo` e retorno o valor mínimo encontrado mais 1 (por conta do quadrado perfeito usado na chamada atual).

E pronto! Mais um exercício resolvido!!