## Número da Coluna da Planilha Excel (Excel Sheet Column Number)

O método `TitleToNumber` converte um título de coluna da planilha Excel em seu número correspondente.

**Funcionamento:**
1. Inicializa o resultado como 0.
2. Para cada caractere no título da coluna:
   - Multiplica o resultado atual por 26 (que é a base do sistema de numeração do Excel).
   - Adiciona o valor do caractere atual (A=1, B=2, ..., Z=26).
3. Retorna o resultado final.

Este processo é análogo à conversão de um número em uma base qualquer para a base decimal. No caso, estamos convertendo da base 26 (onde A=1, B=2, ..., Z=26) para a base decimal.

**Exemplos:**
- Entrada: "A" → Saída: 1
- Entrada: "AB" → Saída: 1×26 + 2 = 28
- Entrada: "ZY" → Saída: 26×26 + 25 = 701

**Complexidade de Tempo:** O(n), onde n é o comprimento do título da coluna.

**Complexidade de Espaço:** O(1), pois utiliza apenas variáveis simples independentemente do tamanho da entrada.
