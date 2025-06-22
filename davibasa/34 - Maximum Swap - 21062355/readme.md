## Maximum Swap

O método `MaximumSwap` recebe um inteiro e retorna o maior valor possível trocando no máximo dois dígitos uma única vez.

**Funcionamento:**

1. Converte o número em um array de caracteres.
2. Armazena o último índice de cada dígito (0-9).
3. Para cada dígito, verifica se existe um dígito maior à direita. Se sim, faz a troca e retorna o novo número.
4. Se não houver troca possível, retorna o número original.

**Exemplo:**

- Entrada: 2736 → Saída: 7236 (troca 2 por 7)
- Entrada: 9973 → Saída: 9973 (nenhuma troca melhora o valor)

**Complexidade de Tempo:** O(d), onde d é o número de dígitos do número.

**Complexidade de Espaço:** O(1), pois o array de índices tem tamanho fixo.
