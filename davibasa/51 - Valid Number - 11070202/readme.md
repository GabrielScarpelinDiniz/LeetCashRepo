## Valid Number

O método `IsNumber` verifica se uma string representa um número válido seguindo as regras de formatação numérica.

### Funcionamento:

1. **Rastreamento de estado**: Monitora se já vimos dígitos, expoente e ponto decimal.
2. **Validação de caracteres**:
   - **Dígitos**: Sempre válidos, marcam que vimos um dígito
   - **Sinais (+/-)**: Válidos apenas no início ou após 'e'/'E'
   - **Ponto decimal**: Válido apenas se não há expoente nem ponto anterior
   - **Expoente (e/E)**: Válido apenas se há dígitos antes e não há expoente anterior
3. **Verificação final**: Deve ter pelo menos um dígito

### Exemplos válidos:

- `"2"`, `"0089"`, `"-0.1"`, `"+3.14"`, `"4."`, `"-.9"`
- `"2e10"`, `"-90E3"`, `"3e+7"`, `"+6e-1"`, `"53.5e93"`

### Exemplos inválidos:

- `"abc"`, `"1a"`, `"1e"`, `"e3"`, `"99e2.5"`, `"--6"`, `"-+3"`

### Complexidade:

- **Tempo:** O(n), onde `n` é o comprimento da string.
- **Espaço:** O(1), usa apenas variáveis booleanas para rastreamento.
