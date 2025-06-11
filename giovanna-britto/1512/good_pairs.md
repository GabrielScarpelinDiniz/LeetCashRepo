# Mais um dia de LeetCash

Hoje eu resolvi o exercício 1512, no qual dado um array de números eu deveria retornar a quantidade de bons pares, no qual um bom par se configura como ``nums[i] == nums[j]``, no qual i < j. Para isso eu segui os seguintes passos:

1. Defino uma variável `cont` para contar a quantidade de pares;
2. For para iterar sobre o array `nums`

    2.1. Segundo for para iterar sobre o array a partir de i+1

    2.2. If para comparar se `nums[i] == nums[j]`, caso seja igual `cont` recebe `cont += 1`

3. Retorna ``cont``

Pronto! Exercício Resolvido!