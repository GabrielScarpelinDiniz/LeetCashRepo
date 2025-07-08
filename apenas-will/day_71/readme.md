## Exercício: 133. Clone Graph
**Objetivo**: Dada um nó de um grafo não direcionado conexo (a partir qualquer nó há um caminho para chegar a qualquer outro nó) crie um cópia dele (criar uma _deep copy_, isto é, apesar dos valores serem iguais, os objetos são diferentes);

## Descrição geral da estratégia
Para resolver aplico um BFS que mapeia cada nó do grafo original para o nó equivalente no novo grafo. Omitirei o processo de implementação do BFS, mas o realizei utilizando uma _queue_ como estrutura auxiliar. Para cada nó visitado na busca em largura, adiciono-o no `oldToNew` (HashMap que mapeia um nó no grafo original para um outro na cópia) caso ele ainda não tenha sido visitado. Caso o HashMap tenha tamanho 1 (ou seja, apenas está lá o primeiro elemento) salvo este elemento numa variável `ans` para retornar ao final. Em seguida, exploro os vizinhos do nó. Caso um vizinho ainda não tenha sido visitado, adiciono-o na fila da busca em largura e crio uma instância para ele no `oldToNew`, após isso, independente do nó ter sido ou não visitado, adiciono (usando o `oldToNew`) registro o nó vizinho na cópia. Repito o processo até ter visitado todos os nós e finalizo retornando `ans`.

## Análise de complexidade
Para um grafo com $v$ nós e $e$ arestas, tem-se:
- **Time complexity**: $O(v + e)$
- **Space complexity**: $O(v)$