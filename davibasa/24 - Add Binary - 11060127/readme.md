## Adição Binária (Add Binary)

O método `AddBinary` soma duas strings binárias e retorna o resultado como uma string binária.

**Funcionamento:**
1. Percorre as strings da direita para a esquerda (como em uma soma manual).
2. Para cada posição, soma os dígitos correspondentes de ambas as strings e o valor do carry.
3. O resultado da soma para cada posição é calculado como `sum % 2`.
4. O carry para a próxima posição é calculado como `sum / 2`.
5. Continua até que todas as posições sejam processadas e não haja mais carry.

**Exemplos:**
- Entrada: a = "11", b = "1"
- Saída: "100"
- Explicação: 3 + 1 = 4 em decimal, ou 11 + 1 = 100 em binário.

- Entrada: a = "1010", b = "1011"
- Saída: "10101"
- Explicação: 10 + 11 = 21 em decimal, ou 1010 + 1011 = 10101 em binário.

**Complexidade de Tempo:** O(max(m, n)), onde m e n são os comprimentos das strings de entrada.

**Complexidade de Espaço:** O(max(m, n)), para armazenar o resultado.
