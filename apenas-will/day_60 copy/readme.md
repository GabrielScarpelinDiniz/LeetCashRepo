## Exercício: 463. Island Perimeter
**Objetivo**: Dada uma matriz de inteiros que representa um mapa, determine o perímetro da ilha presente nesse mapa (0 indica uma região com água, enquanto 1 apresenta uma área com terra);

## Descrição geral da estratégia
Para resolver passo pela matriz buscando um primeiro bloco com solo (fiz duas versões, em uma eu passo de maneira linear e em outra escolhos posições aleatórias). Quando encontro um bloco com solo, realizo uma busca em profundidade, conferindo os blocos adjacentes. Caso eles sejam água, incremento 1 unidade à solução. Caso eles seja, terra, adiciono essas coordenadas à uma matriz de posições visitadas e não incremento nada na solução.

## Análise de complexidade
Para uma matriz $n \times n$, tem-se:
- **Time complexity**: $O(n^2)$
- **Space complexity**: $O(n^2)$