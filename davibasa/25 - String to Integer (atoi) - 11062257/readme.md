## String para Inteiro (atoi)

O método `MyAtoi` implementa a função atoi, que converte uma string em um inteiro de 32 bits com sinal, seguindo estas etapas:

1. **Espaços em branco:** Ignora quaisquer espaços em branco iniciais.
2. **Sinal:** Determina o sinal verificando se o próximo caractere é '-' ou '+', assumindo positivo se nenhum estiver presente.
3. **Conversão:** Lê o inteiro até encontrar um caractere não-dígito ou o fim da string.
4. **Arredondamento:** Se o inteiro estiver fora do intervalo de inteiros de 32 bits com sinal [-2³¹, 2³¹ - 1], arredonda para manter-se no intervalo.

**Exemplos:**
- Entrada: "42" → Saída: 42
- Entrada: " -042" → Saída: -42
- Entrada: "1337c0d3" → Saída: 1337
- Entrada: "words and 987" → Saída: 0
- Entrada: "0-1" → Saída: 0

**Complexidade de Tempo:** O(n), onde n é o comprimento da string.

**Complexidade de Espaço:** O(1), pois utiliza apenas variáveis simples independentemente do tamanho da entrada.
