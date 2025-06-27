## Remove K Digits

O método `RemoveKdigits` recebe uma string `num` representando um número inteiro não negativo e um inteiro `k`. Ele retorna o menor número possível após remover `k` dígitos.

### Funcionamento:

1. Usa uma pilha para construir o menor número possível.
2. Remove os dígitos maiores enquanto percorre a string, garantindo que o número resultante seja o menor possível.
3. Remove dígitos restantes da pilha se `k > 0`.
4. Constrói o número final a partir da pilha e remove zeros à esquerda.

### Exemplos:

- Entrada: `num = "1432219", k = 3` → Saída: `"1219"`
- Entrada: `num = "10200", k = 1` → Saída: `"200"`
- Entrada: `num = "10", k = 2` → Saída: `"0"`

### Complexidade:

- **Tempo:** O(n), onde `n` é o comprimento de `num`.
- **Espaço:** O(n), devido ao uso da pilha.
