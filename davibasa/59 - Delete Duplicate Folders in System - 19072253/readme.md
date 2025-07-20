## Delete Duplicate Folders in System

O método `DeleteDuplicateFolder` remove pastas duplicadas de um sistema de arquivos baseado na estrutura de subpastas.

### Funcionamento:

1. **Construção da Trie**: Constrói uma árvore representando o sistema de arquivos.
2. **Geração de assinaturas**: Cria assinaturas únicas para cada subárvore baseadas na estrutura de subpastas.
3. **Identificação de duplicatas**: Agrupa nós com a mesma assinatura para identificar duplicatas.
4. **Marcação para exclusão**: Marca todas as pastas duplicadas e suas subpastas para exclusão.
5. **Coleta de resultados**: Percorre a árvore coletando apenas caminhos não marcados para exclusão.

### Exemplos:

- Entrada: `paths = [["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]]`
  Saída: `[["d"],["d","a"]]`
- Entrada: `paths = [["a"],["c"],["a","b"],["c","b"],["a","b","x"],["a","b","x","y"],["w"],["w","y"]]`
  Saída: `[["c"],["c","b"],["a"],["a","b"]]`

### Complexidade:

- **Tempo:** O(N × M), onde N é o número de caminhos e M é o comprimento médio dos caminhos.
- **Espaço:** O(N × M) para a estrutura da trie e assinaturas.

### Nota:

A assinatura de uma pasta é determinada pela estrutura ordenada de suas subpastas, permitindo identificar duplicatas estruturais.
