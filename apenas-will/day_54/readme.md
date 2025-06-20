## Exercício: 1971. Find if Path Exists in Graph
**Objetivo**: Dada uma lista de conexões de um grafo, uma fonte e um destino, determine se há um caminho que conecta a fonte ao destino;

## Descrição geral da estratégia
Para resolver implementei um depth-first search recursivo que vai buscando o destino a partir da fonte. Caso o vértice seja encontrado, uma variável de solução é alterada para `true` e a execução da recursão é interrompida, com a variável se mantendo como `false` caso contrário.

## Análise de complexidade
Para um array com $n$ conexões (arestas), tem-se:
- **Time complexity**: $O(n)$
- **Space complexity**: $O(n)$