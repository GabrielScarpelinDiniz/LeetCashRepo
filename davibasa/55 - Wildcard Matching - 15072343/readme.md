## Wildcard Matching

O método `IsMatch` implementa correspondência de padrões wildcard com suporte para '?' e '\*'.

### Funcionamento:

1. **Correspondência direta**: Se caracteres coincidem ou padrão tem '?', avança ambos ponteiros.
2. **Asterisco encontrado**: Registra posição do '\*' e posição atual na string para backtracking.
3. **Backtracking**: Se não há correspondência mas já vimos '\*', volta para tentar mais caracteres.
4. **Finalização**: Pula '\*' restantes no padrão e verifica se foi totalmente consumido.

### Caracteres especiais:

- **'?'**: Corresponde a qualquer caractere único
- **'\*'**: Corresponde a qualquer sequência de caracteres (incluindo vazia)

### Exemplos:

- Entrada: `s = "aa", p = "a"` → Saída: `false`
- Entrada: `s = "aa", p = "*"` → Saída: `true`
- Entrada: `s = "cb", p = "?a"` → Saída: `false`

### Complexidade:

- **Tempo:** O(s × p) no pior caso, O(s + p) no caso médio.
- **Espaço:** O(1), usa apenas variáveis auxiliares.

### Vantagem:

Este algoritmo iterativo é mais eficiente que a abordagem de programação dinâmica tradicional.
