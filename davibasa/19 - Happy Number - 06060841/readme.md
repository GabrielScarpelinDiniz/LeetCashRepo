## Número Feliz (Happy Number)

O método `IsHappy` determina se um número é feliz. Um número é considerado feliz se, ao substituir o número pela soma dos quadrados de seus dígitos repetidamente, eventualmente chega-se ao número 1. Caso contrário, entra-se em um ciclo infinito que não inclui o 1.

**Funcionamento:**

1. Utiliza um conjunto (HashSet) para rastrear números já vistos e detectar ciclos.
2. Calcula a soma dos quadrados dos dígitos do número atual.
3. Repete o processo até encontrar 1 (feliz) ou detectar um ciclo (não feliz).

**Exemplo:**

- Entrada: 19
- Saída: true
- Processo: 1² + 9² = 82 → 8² + 2² = 68 → 6² + 8² = 100 → 1² + 0² + 0² = 1

**Complexidade de Tempo:** O(log n), pois o número de iterações é limitado pelo ciclo dos dígitos.

**Complexidade de Espaço:** O(log n), para armazenar os números já vistos.
