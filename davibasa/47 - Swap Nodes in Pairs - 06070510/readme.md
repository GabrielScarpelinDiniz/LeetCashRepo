## Swap Nodes in Pairs

O método `SwapPairs` troca os nós de uma lista ligada dois a dois, sem alterar os valores dos nós.

### Funcionamento:

1. Usa um nó sentinela (`dummy`) para facilitar a manipulação do início da lista.
2. Percorre a lista, trocando os pares de nós adjacentes.
3. Ajusta os ponteiros para manter a lista ligada corretamente.
4. Retorna o novo início da lista.

### Exemplos:

- Entrada: `head = [1,2,3,4]` → Saída: `[2,1,4,3]`
- Entrada: `head = []` → Saída: `[]`
- Entrada: `head = [1]` → Saída: `[1]`
- Entrada: `head = [1,2,3]` → Saída: `[2,1,3]`

### Complexidade:

- **Tempo:** O(n), onde `n` é o número de nós da lista.
- **Espaço:** O(1), pois a troca é feita in-place.
