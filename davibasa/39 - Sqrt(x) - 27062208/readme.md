## Sqrt(x)

O método `MySqrt` calcula a raiz quadrada inteira de um número não negativo `x` sem usar funções matemáticas embutidas.

### Funcionamento:

1. Usa busca binária para encontrar o maior número `mid` tal que `mid * mid <= x`.
2. Ajusta os limites esquerdo (`left`) e direito (`right`) com base na comparação de `mid * mid` com `x`.
3. Retorna o valor arredondado para baixo.

### Exemplos:

- Entrada: `x = 4` → Saída: `2`
- Entrada: `x = 8` → Saída: `2`

### Complexidade:

- **Tempo:** O(log x), devido à busca binária.
- **Espaço:** O(1), pois não utiliza espaço adicional significativo.
