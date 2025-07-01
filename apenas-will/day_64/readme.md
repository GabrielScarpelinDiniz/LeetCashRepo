## Exercício: 733. Flood Fill
**Objetivo**: Dada uma matriz inteiros que representa uma imagem, um pixel de início e uma cor, altere todas os pixels adjacentes àquele pixel pela cor dada;

## Descrição geral da estratégia
Para resolver aplico um DFS que vai alterando as cores de todos os pixels adjacentes, salvando aqueles já modificados em uma matriz auxiliar de visitados.

## Análise de complexidade
Para uma matriz $n \times m$, tem-se:
- **Time complexity**: $O(n \times m)$
- **Space complexity**: $O(n \times m)$