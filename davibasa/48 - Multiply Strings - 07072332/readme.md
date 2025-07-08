## Multiply Strings

O método `Multiply` multiplica dois números inteiros não negativos representados como strings, sem converter para inteiro nem usar BigInteger.

### Funcionamento:

1. Cria um array para armazenar os resultados parciais de cada multiplicação de dígitos.
2. Multiplica cada dígito de `num1` por cada dígito de `num2` e soma nos índices corretos do array.
3. Ajusta os "vai uns" (carry) para cada posição.
4. Constrói a string resultado ignorando zeros à esquerda.

### Exemplos:

- Entrada: `num1 = "2", num2 = "3"` → Saída: `"6"`
- Entrada: `num1 = "123", num2 = "456"` → Saída: `"56088"`

### Complexidade:

- **Tempo:** O(m × n), onde `m` e `n` são os tamanhos das strings.
- **Espaço:** O(m + n), para o array intermediário.

Se precisar de mais alguma coisa, é só avisar! 🚀
