# Dia tantos de LeetCash

Gente, estou com sono e sem cabeça para escrever, então segue a resolução do problema do tipo de triângulo (3024):

1. Recebo um array `nums` com 3 inteiros representando os lados de um triângulo.
2. Atribuo os valores de `nums` às variáveis `a`, `b` e `c`.
3. Verifico se esses três lados formam um triângulo usando a **inequação triangular**:
   * Se **não** formam um triângulo (`a + b <= c`, etc), retorno `"none"`
4. Se passaram no teste, verifico: 
   * Se os três lados são **iguais**, retorno `"equilateral"`.
   * Se só **dois** lados são iguais, retorno `"isosceles"`.
   * Se **todos diferentes**, é o famoso `"scalene"`.

E exercício resolvido, Boa noite galerinha, até amanhã!!
