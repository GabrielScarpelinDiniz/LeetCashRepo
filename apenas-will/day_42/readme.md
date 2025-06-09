## Exercício: 1791. Find Center of Star Graph
**Objetivo**: Dada uma lista de arestas de um grafo estrela (grafo no qual todos os vértices estão conectados a um vértice central) determine qual é o vértice central;

## Descrição geral da estratégia
Para resolver implementei uma abordagem que itera pela lista de arestas, contando o número de vezes que cada vértice aparece. Em seguida, itero pela lista com as contagens e retorno o nó que possui mais conexões (o nó central). 

## Análise de complexidade
Para uma lista com $n$ arestas, tem-se:
- **Time complexity**: $O(n)$ 
- **Space complexity**: $O(n)$

## OBS
Após resolver o exercício, fiquei curioso de como poderia melhorar a complexidade da solução. Nesse contexto, vi uma forma alternativa de entender o problema e construí a seguinte solução é capaz de resolvê-lo em $O(1)$ de complexidade de espaço e tempo:

```java
class Solution {
    public int findCenter(int[][] edges) {
        int res = 0;

        if(edges[0][0] == edges[1][0]){
            res = edges[0][0];
        } else if (edges[0][0] == edges[1][1]){
            res = edges[0][0];
        } else if (edges[0][1] == edges[1][0]){
            res = edges[0][1];
        } else if (edges[0][1] == edges[1][1]){
            res = edges[0][1];
        }

        return res;
    }
}
```