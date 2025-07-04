## Median of Two Sorted Arrays

O método `FindMedianSortedArrays` encontra a mediana de dois arrays ordenados em complexidade O(log(m+n)).

### Funcionamento:

1. **Garantir otimização**: Assegura que `nums1` seja o menor array para otimizar a busca binária.
2. **Particionamento**: Divide os arrays em duas partes de tamanhos iguais (ou quase iguais).
3. **Busca binária**: Encontra a partição correta onde todos os elementos da esquerda são menores que os da direita.
4. **Cálculo da mediana**:
   - Se o total de elementos é par: média dos dois elementos centrais
   - Se ímpar: o elemento central

### Exemplos:

- Entrada: `nums1 = [1,3], nums2 = [2]`

  - Array mesclado: `[1,2,3]`
  - Saída: `2.00000`

- Entrada: `nums1 = [1,2], nums2 = [3,4]`
  - Array mesclado: `[1,2,3,4]`
  - Saída: `2.50000` (média de 2 e 3)

### Complexidade:

- **Tempo:** O(log(min(m,n))), onde `m` e `n` são os tamanhos dos arrays.
- **Espaço:** O(1), usa apenas variáveis auxiliares.

### Vantagem:

Este algoritmo é mais eficiente que mesclar os arrays (O(m+n)) usando busca binária inteligente.
