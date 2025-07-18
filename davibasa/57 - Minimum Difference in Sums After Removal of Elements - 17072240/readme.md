## Minimum Difference in Sums After Removal of Elements

O método `MinimumDifference` encontra a diferença mínima entre as somas de duas partes após remover n elementos de um array de tamanho 3n.

### Funcionamento:

1. **Estratégia**: Para minimizar `sumfirst - sumsecond`, precisamos minimizar `sumfirst` e maximizar `sumsecond`.
2. **Pré-processamento**:
   - Calcula a soma mínima dos primeiros n elementos considerando elementos adicionais da esquerda
   - Calcula a soma máxima dos últimos n elementos considerando elementos adicionais da direita
3. **Priority Queues**:
   - Max heap para manter os n menores elementos na primeira parte
   - Min heap para manter os n maiores elementos na segunda parte
4. **Busca**: Testa todas as posições possíveis de divisão para encontrar a diferença mínima.

### Exemplos:

- Entrada: `nums = [3,1,2]` → Saída: `-1`
- Entrada: `nums = [7,9,5,8,1,3]` → Saída: `1`

### Complexidade:

- **Tempo:** O(n log n), onde n é nums.length / 3.
- **Espaço:** O(n) para as estruturas auxiliares.

### Nota:

Esta solução usa heaps para manter eficientemente os n melhores elementos em cada parte.
