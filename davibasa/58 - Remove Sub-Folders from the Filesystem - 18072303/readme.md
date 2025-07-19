## Remove Sub-Folders from the Filesystem

O método `RemoveSubfolders` remove todas as subpastas de uma lista de pastas, mantendo apenas as pastas principais.

### Funcionamento:

1. **Ordenação**: Ordena as pastas lexicograficamente para que pastas pais venham antes de suas subpastas.
2. **Verificação sequencial**: Percorre a lista ordenada, verificando se cada pasta é subpasta da anterior.
3. **Critério de subpasta**: Uma pasta é subpasta se começa com a pasta anterior + "/".
4. **Filtragem**: Adiciona ao resultado apenas pastas que não são subpastas.

### Exemplos:

- Entrada: `folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]`
  Saída: `["/a","/c/d","/c/f"]`
- Entrada: `folder = ["/a","/a/b/c","/a/b/d"]`
  Saída: `["/a"]`
- Entrada: `folder = ["/a/b/c","/a/b/ca","/a/b/d"]`
  Saída: `["/a/b/c","/a/b/ca","/a/b/d"]`

### Complexidade:

- **Tempo:** O(n log n), devido à ordenação das strings.
- **Espaço:** O(n) para armazenar o resultado.

### Nota:

A ordenação lexicográfica garante que pastas pais sempre apareçam antes de suas subpastas.
