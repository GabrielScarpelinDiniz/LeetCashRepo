# Quase 50 dias de LeetCash

Hoje eu resolvi o exercício 1534, que pede para contar quantos "good triplets" existem em um array. Um triplet (i, j, k) é considerado bom se i < j < k e as diferenças entre os elementos respeitam os limites a, b e c. Para isso eu segui os seguintes passos:

1. Criei uma variável `cont` para contar quantos triplets bons encontrei.
2. Usei três fors para pegar todas as combinações possíveis de índices i, j, k com i < j < k.
3. Para cada triplet, verifiquei se:
    - `abs(arr[i] - arr[j]) <= a`
    - `abs(arr[j] - arr[k]) <= b`
    - `abs(arr[i] - arr[k]) <= c`
4. Se todas as condições forem verdadeiras, aumento o contador `cont`.
5. No final, retorno o valor de `cont` com a quantidade de triplets bons.

E pronto! Mais um exercício resolvido!!