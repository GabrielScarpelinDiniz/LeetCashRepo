## Enésimo Número Tribonacci (N-th Tribonacci Number)

O método `Tribonacci` calcula o enésimo número da sequência de Tribonacci, que é definida da seguinte forma:

- T0 = 0
- T1 = 1
- T2 = 1
- Tn+3 = Tn + Tn+1 + Tn+2 para n >= 0

**Funcionamento:**

1. Trata os casos base: T0 = 0, T1 = 1, T2 = 1.
2. Utiliza um array para armazenar os valores já calculados (programação dinâmica).
3. Calcula cada número subsequente como a soma dos três números anteriores.

**Exemplo:**

- Entrada: n = 4
- Saída: 4
- Cálculo:
  - T0 = 0
  - T1 = 1
  - T2 = 1
  - T3 = 0 + 1 + 1 = 2
  - T4 = 1 + 1 + 2 = 4

**Complexidade de Tempo:** O(n), pois calcula cada número exatamente uma vez.

**Complexidade de Espaço:** O(n), para armazenar os números da sequência já calculados.
