## Maximize Subarrays After Removing One Conflicting Pair

O método `MaximizeSubarrays` encontra o número máximo de subarrays válidos após remover exatamente um par conflitante.

### Funcionamento:

1. **Tentativa de remoção**: Testa a remoção de cada par conflitante um por vez.
2. **Contagem de subarrays**: Para cada configuração, conta todos os subarrays válidos.
3. **Validação**: Um subarray é válido se não contém ambos os elementos de nenhum par conflitante restante.
4. **Maximização**: Retorna o maior número de subarrays válidos encontrado.

### Exemplos:

- Entrada: `n = 4, conflictingPairs = [[2,3],[1,4]]`
  - Remove `[2,3]`: 9 subarrays válidos
  - Saída: `9`
- Entrada: `n = 5, conflictingPairs = [[1,2],[2,5],[3,5]]`
  - Remove `[1,2]`: 12 subarrays válidos
  - Saída: `12`

### Complexidade:

- **Tempo:** O(k × n² × k), onde k é o número de pares conflitantes e n é o tamanho do array.
- **Espaço:** O(k) para armazenar os pares restantes.

### Nota:

A solução usa força bruta para testar todas as possibilidades de remoção e validação, garantindo encontrar o resultado ótimo.
