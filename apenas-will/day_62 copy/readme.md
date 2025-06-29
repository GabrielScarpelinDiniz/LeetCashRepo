## Exercício: 200. Number of Islands
**Objetivo**: Dada uma matriz de caracteres que representa um mapa, determine quantas ilhas existem nesse mapa ('0' indica uma região com água, enquanto '1' apresenta uma área com terra);

## Descrição geral da estratégia
Para resolver passo pela matriz buscando um primeiro bloco com solo. Quando encontro um bloco com solo, incremento a contagem de ilhas e realizo uma busca em profundidade conferindo os blocos adjacentes. Caso eles sejam água, retorno, mas, caso eles sejam terra, removo-os do mapa (mudando seu valor para 0) para evitar contagens múltiplas. Repito esse processo até chegar ao final do mapa, retornando a quantidade de ilhas.

## Análise de complexidade
Para uma matriz $n \times m$, tem-se:
- **Time complexity**: $O(n \times m)$
- **Space complexity**: $O(i)$