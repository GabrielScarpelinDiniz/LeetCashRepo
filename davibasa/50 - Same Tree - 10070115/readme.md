## Same Tree

O método `IsSameTree` verifica se duas árvores binárias são estruturalmente idênticas e têm os mesmos valores nos nós.

### Funcionamento:

1. **Casos base**: Se ambas as árvores são vazias, retorna `true`.
2. **Verificação de nulidade**: Se apenas uma árvore é vazia, retorna `false`.
3. **Comparação de valores**: Verifica se os valores dos nós atuais são iguais.
4. **Recursão**: Compara recursivamente as subárvores esquerda e direita.

### Exemplos:

- Entrada: `p = [1,2,3], q = [1,2,3]` → Saída: `true`
- Entrada: `p = [1,2], q = [1,null,2]` → Saída: `false`
- Entrada: `p = [1,2,1], q = [1,1,2]` → Saída: `false`

### Complexidade:

- **Tempo:** O(min(m,n)), onde `m` e `n` são os números de nós nas árvores.
- **Espaço:** O(min(m,n)), devido à pilha de chamadas recursivas.
