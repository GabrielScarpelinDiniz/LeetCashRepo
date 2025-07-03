## Zigzag Conversion

O método `Convert` converte uma string em um padrão zigzag com um número específico de linhas e retorna a string lida linha por linha.

### Funcionamento:

1. **Casos especiais**: Se `numRows = 1` ou a string é menor que o número de linhas, retorna a string original.
2. **Inicialização**: Cria um array de `StringBuilder` para cada linha.
3. **Padrão zigzag**: Usa uma variável `goingDown` para alternar a direção ao alcançar o topo ou fundo.
4. **Construção**: Adiciona cada caractere à linha apropriada seguindo o padrão.
5. **Resultado**: Concatena todas as linhas para formar a string final.

### Exemplos:

- Entrada: `s = "PAYPALISHIRING", numRows = 3`

  ```
  P   A   H   N
  A P L S I I G
  Y   I   R
  ```

  Saída: `"PAHNAPLSIIGYIR"`

- Entrada: `s = "PAYPALISHIRING", numRows = 4`

  ```
  P     I    N
  A   L S  I G
  Y A   H R
  P     I
  ```

  Saída: `"PINALSIGYAHRPI"`

- Entrada: `s = "A", numRows = 1`
  Saída: `"A"`

### Complexidade:

- **Tempo:** O(n), onde `n` é o comprimento da string.
- **Espaço:** O(n) para armazenar os `StringBuilder` de cada linha.
