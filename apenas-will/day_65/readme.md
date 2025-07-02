## Exercício: 1034. Coloring A Border
**Objetivo**: Dada uma matriz inteiros que representa uma imagem, um pixel de início e uma cor,altere a cor dos pixels de borda do componente conexo ao qual àquele pixel inicial faz parte;

## Descrição geral da estratégia
Para resolver aplico um DFS que vai alterando as cores de todos os pixels identificados como borda (que possuem pixels de cores diferentes ao seu redor ou que estão na borda da imagem), salvando aqueles já modificados em uma matriz auxiliar de visitados.

## Análise de complexidade
Para uma matriz $n \times m$, tem-se:
- **Time complexity**: $O(n \times m)$
- **Space complexity**: $O(n \times m)$