## Classificações Relativas (Relative Ranks)

O método `FindRelativeRanks` atribui posições relativas a atletas com base em suas pontuações.

**Funcionamento:**

1. Clona e ordena o array `score` em ordem decrescente.
2. Mapeia cada pontuação à sua classificação (1º, 2º, 3º, etc.).
3. Itera pelo array original e converte a classificação em string:
   - 1 → "Gold Medal"
   - 2 → "Silver Medal"
   - 3 → "Bronze Medal"
   - Demais → posição numérica ("4", "5", ...)

**Exemplos:**

- Entrada: [5,4,3,2,1] → ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
- Entrada: [10,3,8,9,4] → ["Gold Medal","5","Bronze Medal","Silver Medal","4"]

**Complexidade de Tempo:** O(n log n), devido à ordenação.

**Complexidade de Espaço:** O(n), para o array e o dicionário auxiliares.
