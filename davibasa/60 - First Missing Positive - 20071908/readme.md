## First Missing Positive

O método `FirstMissingPositive` encontra o menor inteiro positivo que não está presente no array, usando O(n) tempo e O(1) espaço.

### Funcionamento:
1. **Normalização**: Substitui números inválidos (≤ 0 ou > n) por n+1.
2. **Marcação**: Usa o sinal dos elementos para marcar a presença de números de 1 a n.
3. **Busca**: Encontra o primeiro índice com valor positivo, indicando o número ausente.
4. **Caso especial**: Se todos os números de 1 a n estão presentes, retorna n+1.

### Técnica:
- Usa o próprio array como estrutura de dados auxiliar
- Transforma números em índices: número `x` marca posição `x-1`
- Usa sinais negativos para marcar presença sem perder informação

### Exemplos:
- Entrada: `nums = [1,2,0]` → Saída: `3`
- Entrada: `nums = [3,4,-1,1]` → Saída: `2`
- Entrada: `nums = [7,8,9,11,12]` → Saída: `1`

### Complexidade:
- **Tempo:** O(n), três passadas pelo array.
- **Espaço:** O(1), modifica o array in-place.

### Nota:
Esta é uma solução elegante que usa o array como hash table improvisado para atender às restrições de complexidade.
