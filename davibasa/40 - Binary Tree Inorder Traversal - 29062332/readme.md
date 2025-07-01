## Binary Tree Inorder Traversal

O método `InorderTraversal` realiza a travessia em ordem de uma árvore binária e retorna os valores dos nós em uma lista.

### Funcionamento:

1. Usa um método recursivo auxiliar `Inorder` para visitar os nós na ordem: esquerda, raiz, direita.
2. Adiciona os valores dos nós visitados a uma lista de resultados.
3. Retorna a lista de resultados após a travessia completa.

### Exemplos:

- Entrada: `root = [1,null,2,3]` → Saída: `[1,3,2]`
- Entrada: `root = [1,2,3,4,5,null,8,null,null,6,7,9]` → Saída: `[4,2,6,5,7,1,3,9,8]`
- Entrada: `root = []` → Saída: `[]`
- Entrada: `root = [1]` → Saída: `[1]`

### Complexidade:

- **Tempo:** O(n), onde `n` é o número de nós na árvore.
- **Espaço:** O(h), onde `h` é a altura da árvore, devido à pilha de chamadas recursivas.
