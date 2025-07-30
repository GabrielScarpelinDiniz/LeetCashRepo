## Longest Subarray With Maximum Bitwise AND

O método `LongestSubarray` encontra o comprimento do maior subarray contíguo com o AND bit a bit máximo possível.

### Funcionamento:

1. **Encontra o valor máximo**: O AND máximo de qualquer subarray é igual ao maior elemento do array.
2. **Conta elementos consecutivos**: Procura a maior sequência consecutiva de elementos iguais ao máximo.
3. **Retorna o comprimento**: O maior subarray encontrado.

### Insight:

O AND bit a bit de um subarray nunca pode ser maior que o maior elemento do array, pois o AND só pode diminuir ou manter bits. Portanto, o AND máximo é sempre igual ao maior elemento.

### Exemplos:

- Entrada: `nums = [1,2,3,3,2,2]` → Saída: `2`
  - Valor máximo: 3
  - Maior sequência de 3s consecutivos: [3,3] (comprimento 2)
- Entrada: `nums = [1,2,3,4]` → Saída: `1`
  - Valor máximo: 4
  - Maior sequência de 4s consecutivos: [4] (comprimento 1)

### Complexidade:

- **Tempo:** O(n), duas passadas pelo array.
- **Espaço:** O(1), apenas variáveis auxiliares.

### Nota:

Esta é uma solução otimizada que utiliza a propriedade do AND bit a bit para evitar calcular todos os subarrays possíveis.
