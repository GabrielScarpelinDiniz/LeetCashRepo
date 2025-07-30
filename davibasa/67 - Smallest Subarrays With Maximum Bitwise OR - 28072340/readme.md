## Smallest Subarrays With Maximum Bitwise OR

O método `SmallestSubarrays` encontra, para cada posição inicial, o menor subarray que alcança o OR bit a bit máximo possível.

### Funcionamento:

1. **Para cada posição inicial i**:
   - Calcula o OR máximo possível considerando todos os subarrays que começam em i
   - Encontra o menor subarray que atinge esse OR máximo
2. **Duas passadas**:
   - Primeira: determina o OR máximo possível
   - Segunda: encontra o menor subarray que atinge esse máximo

### Exemplos:

- Entrada: `nums = [1,0,2,1,3]` → Saída: `[3,3,2,2,1]`
- Entrada: `nums = [1,2]` → Saída: `[2,1]`

### Complexidade:

- **Tempo:** O(n²), onde n é o tamanho do array.
- **Espaço:** O(1) adicional, desconsiderando o array de resultado.

### Nota:

O OR bit a bit é monotônico crescente, então uma vez que atingimos o máximo, não precisamos continuar expandindo o subarray.
