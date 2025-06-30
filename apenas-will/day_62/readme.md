## Exercício: 695. Max Area of Island
**Objetivo**: Dada uma matriz de inteiros que representa um mapa, determine a área da maior ilha desse mapa (0 indica uma região com água, enquanto 1 apresenta uma área com terra);

## Descrição geral da estratégia
Para resolver passo pela matriz buscando um primeiro bloco com solo. Quando encontro um bloco com solo, realizo uma busca em profundidade, conferindo os blocos adjacentes. Caso eles sejam água, retorno, mas, caso eles sejam terra, adiciono essas coordenadas à uma matriz de posições visitadas e incremento a área da ilha em uma unidade. Repito esse processo até chegar ao final do mapa, retornando a área da maior ilha encontrada.

## Análise de complexidade
Para uma matriz $n \times m$, tem-se:
- **Time complexity**: $O(n \times m)$
- **Space complexity**: $O(n \times m)$