## Valid Parentheses

O método `IsValid` verifica se uma string composta apenas por parênteses, colchetes e chaves está corretamente balanceada.

### Funcionamento:

1. Usa uma pilha para armazenar os caracteres de abertura.
2. Para cada caractere de fechamento, verifica se corresponde ao topo da pilha.
3. Retorna `true` se todos os pares forem válidos e a pilha estiver vazia ao final.

### Exemplos:

- Entrada: `s = "()"` → Saída: `true`
- Entrada: `s = "()[]{}"` → Saída: `true`
- Entrada: `s = "(]"` → Saída: `false`
- Entrada: `s = "([])"` → Saída: `true`

### Complexidade:

- **Tempo:** O(n), onde `n` é o comprimento da string.
- **Espaço:** O(n), no pior caso, para a pilha.
