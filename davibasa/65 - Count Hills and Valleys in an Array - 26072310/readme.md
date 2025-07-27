## Count Hills and Valleys in an Array

O método `CountHillValley` conta o número de colinas e vales em um array, considerando grupos de elementos iguais como parte do mesmo relevo.

### Funcionamento:

1. **Busca dos vizinhos não iguais**: Para cada posição, encontra o vizinho diferente mais próximo à esquerda e à direita.
2. **Critério de colina**: O valor é maior que ambos os vizinhos não iguais.
3. **Critério de vale**: O valor é menor que ambos os vizinhos não iguais.
4. **Agrupamento**: Avança o índice para o próximo grupo diferente após processar um grupo de iguais.

### Exemplos:

- Entrada: `nums = [2,4,1,1,6,5]` → Saída: `3`
- Entrada: `nums = [6,6,5,5,4,1]` → Saída: `0`

### Complexidade:

- **Tempo:** O(n), onde n é o tamanho do array.
- **Espaço:** O(1), apenas variáveis auxiliares.

### Nota:

O algoritmo garante que colinas e vales consecutivos de elementos iguais sejam contados apenas uma vez.
