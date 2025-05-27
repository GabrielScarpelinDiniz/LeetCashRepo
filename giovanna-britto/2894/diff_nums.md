# Dia 29 de Leet Cash

Boa noite Pessoal! Espero que estejam todos bem, porque eu não estou, mesmo assim ainda não desisti da competição. Hoje eu resolvi o exercício 2894, na qual dado um número `n` e um `m` como entrada eu deveria retornar a subtração entre a soma de todos os valores de 1 até n que eram divisíveis por m e a soma de todos os valores de 1 até n que não eram divisíveis por m. Sendo assim para resolver esse exercício, eu segui os seguintes passos:

1. Criei os arrays para armazenar os números divisíveis `numDiv` e os não divisiveis `numNdiv`
2. For que itera de 1 até n+1, onde verifica se:
    - O resto da divisão de i por m é igual a zero: adiciona i a `numDiv`
    - O resto da divisão de i por m é diferente de zero: adiciona i a `numNDiv`
3. Atribui a soma de `numNDiv` à num1
4. Atribui a soma de `numDiv` à num2
5. Retorna `int(num1- num2)`

Sendo assim, temos mais um exercício resolvido!!!