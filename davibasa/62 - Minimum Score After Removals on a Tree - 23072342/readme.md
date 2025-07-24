## Minimum Score After Removals on a Tree

O método `MinimumScore` encontra a pontuação mínima após remover duas arestas de uma árvore, criando três componentes conectados.

### Funcionamento:

1. **Construção do grafo**: Cria lista de adjacência a partir das arestas.
2. **Cálculo de XOR de subárvores**: Pré-calcula o XOR de cada subárvore usando DFS.
3. **Tentativa de todas as combinações**: Testa todos os pares possíveis de remoção de arestas.
4. **Simulação de remoção**: Para cada par, simula a remoção e calcula os componentes resultantes.
5. **Cálculo da pontuação**: Para cada configuração válida (3 componentes), calcula a diferença entre maior e menor XOR.

### Exemplos:

- Entrada: `nums = [1,5,5,4,11], edges = [[0,1],[1,2],[1,3],[3,4]]`
  Saída: `9`
- Entrada: `nums = [5,5,2,4,4,2], edges = [[0,1],[1,2],[5,2],[4,3],[1,3]]`
  Saída: `0`

### Complexidade:

- **Tempo:** O(n³), onde n é o número de nós (testando todos os pares de arestas).
- **Espaço:** O(n) para estruturas auxiliares.

### Nota:

A solução usa DFS para simular a remoção de arestas e calcular os XORs dos componentes resultantes, garantindo que exatamente 3 componentes sejam formados.
