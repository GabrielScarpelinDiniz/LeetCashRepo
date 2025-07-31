# 898. Bitwise ORs of Subarrays

## Problema

Dado um array de inteiros `arr`, retorne o número de ORs bit a bit distintos de todos os subarrays não vazios de `arr`.

O OR bit a bit de um subarray é o OR bit a bit de cada inteiro no subarray. O OR bit a bit de um subarray de um único inteiro é esse inteiro.

Um subarray é uma sequência contígua não vazia de elementos dentro de um array.

### Exemplo 1:

**Entrada:** `arr = [0]`

**Saída:** `1`

**Explicação:** Há apenas um resultado possível: `0`.

### Exemplo 2:

**Entrada:** `arr = [1,1,2]`

**Saída:** `3`

**Explicação:** Os subarrays possíveis são `[1]`, `[1]`, `[2]`, `[1, 1]`, `[1, 2]`, `[1, 1, 2]`. Estes produzem os resultados `1`, `1`, `2`, `1`, `3`, `3`. Há 3 valores únicos, então a resposta é `3`.

### Exemplo 3:

**Entrada:** `arr = [1,2,4]`

**Saída:** `6`

**Explicação:** Os resultados possíveis são `1`, `2`, `3`, `4`, `6` e `7`.

### Restrições:

- `1 <= arr.length <= 5 * 10^4`
- `0 <= arr[i] <= 10^9`

## Solução

A solução utiliza conjuntos (`HashSet`) para armazenar os resultados únicos de ORs bit a bit. Para cada número no array, calculamos o OR com os resultados do conjunto atual e adicionamos ao próximo conjunto. No final, retornamos o tamanho do conjunto de resultados.

### Complexidade

- **Tempo:** O(n^2) no pior caso, onde n é o tamanho do array.
- **Espaço:** O(n) para armazenar os resultados intermediários.
