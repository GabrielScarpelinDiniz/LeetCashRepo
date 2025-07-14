## Random Flip Matrix

A classe `Solution` implementa uma matriz binária que permite escolher aleatoriamente células com valor 0 e alterá-las para 1.

### Funcionamento:

1. **Mapeamento virtual**: Usa um dicionário para mapear índices já utilizados.
2. **Algoritmo de Fisher-Yates**: Adapta o algoritmo de embaralhamento para evitar armazenar toda a matriz.
3. **Remapeamento**: Quando um índice é escolhido, ele é mapeado para o último índice disponível.
4. **Reset**: Limpa o mapeamento e restaura o total de células disponíveis.

### Métodos:

- **`Solution(m, n)`**: Inicializa uma matriz m×n.
- **`Flip()`**: Retorna um índice aleatório [i, j] onde matrix[i][j] == 0 e o converte para 1.
- **`Reset()`**: Redefine todos os valores da matriz para 0.

### Exemplo:

```
Solution solution = new Solution(3, 1);
solution.Flip();  // return [1, 0]
solution.Flip();  // return [2, 0]
solution.Flip();  // return [0, 0]
solution.Reset(); // Reset all values
solution.Flip();  // return [2, 0]
```

### Complexidade:

- **Tempo:** O(1) para `Flip()` e `Reset()`.
- **Espaço:** O(k), onde k é o número de células já utilizadas.
