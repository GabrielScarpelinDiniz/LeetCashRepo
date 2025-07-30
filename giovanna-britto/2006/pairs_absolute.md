# Mais um dia de Leetcash

Hoje eu resolvi o exercício 2006, em que dado uma lista de inteiros eu deveria dizer a quantidade de pares (i,j) em que o valor absoluto da subtração deles resultaria em um valor igual a k. Para isso eu segui os seguintes passos:

1. Defini uma variável `cont` para contar a quantidade de pares;

2. For para iterar em i sob os valores de nums;

3. Segundo for para iterar em j, a partir de ``i+1``.

4. If para verificar se `abs(nums[i] - nums[j] == k )` e caso seja verdadeiro soma mais um em cont.

5. Retorna o valor de `cont`.

E pronto! Mais um exercício resolvido!!