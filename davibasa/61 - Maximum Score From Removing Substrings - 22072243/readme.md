## Maximum Score From Removing Substrings

O método `MaximumGain` calcula a pontuação máxima removendo substrings "ab" e "ba" de uma string.

### Funcionamento:

1. **Estratégia gulosa**: Remove primeiro a substring que dá mais pontos para maximizar o resultado.
2. **Uso de pilha**: Para cada substring, usa uma pilha para identificar e remover pares de caracteres.
3. **Duas passadas**: Primeira passada remove a substring de maior valor, segunda remove a de menor valor.
4. **Atualização da string**: Reconstrói a string após cada remoção para a próxima iteração.

### Exemplos:

- Entrada: `s = "cdbcbbaaabab", x = 4, y = 5`
  - Remove "ba" primeiro (y=5 > x=4)
  - Saída: `19`
- Entrada: `s = "aabbaaxybbaabb", x = 5, y = 4`
  - Remove "ab" primeiro (x=5 > y=4)
  - Saída: `20`

### Complexidade:

- **Tempo:** O(n), onde n é o comprimento da string.
- **Espaço:** O(n) para a pilha no pior caso.

### Nota:

A estratégia gulosa funciona porque remover a substring de maior valor primeiro sempre resulta na pontuação máxima ou igual comparada a qualquer outra ordem.
