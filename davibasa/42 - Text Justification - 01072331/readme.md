## Text Justification

O método `FullJustify` formata um array de palavras em linhas justificadas com largura específica.

### Funcionamento:

1. **Agrupamento de palavras**: Determina quantas palavras cabem em cada linha.
2. **Justificação completa**: Distribui espaços uniformemente entre as palavras (exceto última linha).
3. **Justificação à esquerda**: Para a última linha e linhas com uma única palavra.
4. **Distribuição de espaços**: Espaços extras são distribuídos da esquerda para a direita.

### Exemplos:

- Entrada: `words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16`
  Saída:

  ```
  "This    is    an"
  "example  of text"
  "justification.  "
  ```

- Entrada: `words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16`
  Saída:
  ```
  "What   must   be"
  "acknowledgment  "
  "shall be        "
  ```

### Complexidade:

- **Tempo:** O(n × m), onde `n` é o número de palavras e `m` é a largura máxima.
- **Espaço:** O(m) para a construção de cada linha.
