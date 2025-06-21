## Exercício: 207. Course Schedule
**Objetivo**: Dada uma lista de dependências entre cursos, determine se há alguma ordenação de cursos em que todas as dependências possam ser respeitadas (suponha que o curso $1$ exige a conclusão do curso $0$. Se houver apenas essa dependência, a ordem $0 \rarr 1$ é válida. Porém, caso o curso $0$ precise também do curso $1$ é impossível ordenar esses cursos, pois isso geraria um loop);

## Descrição geral da estratégia
Para resolver implementei um algoritmo de detecção de ciclos em grafos usando depth-first search recursivo. Nesse contexto, caso um loop seja encontrado, o algoritmo retorna `true` e, portanto, o resultado da existência de ordenação é `false` e vice-versa.

## Análise de complexidade
Para um array com $e$ conexões (arestas) e $n$ vértices, tem-se:
- **Time complexity**: $O(e)$
- **Space complexity**: $O(n)$