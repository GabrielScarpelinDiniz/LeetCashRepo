## Exercício: 210. Course Schedule II
**Objetivo**: Dada uma quantidade de cursos e uma listas de pré-requisitos ([0, 1] indica que o curso 1 é pré-requisito para realizar o curso 0) determine uma ordenação possível para que todos os cursos sejam realizados respeitando os pré-requisitos;

## Descrição geral da estratégia
Para resolver usei o algoritmo de Khan para geração de ordenações topológicas em grafos direcionados acíclicos (DAGs). Para começar, modelei o problema como um grafo direcionado, no qual as arestas $u \rightarrow v$ indica que o curso $u$ é pré-requisito do curso $v$. Após isso, criei uma lista auxiliar `inDegree` que salva o número de arestas de entrada em cada vértice do grafo (no contexto do problema, salva quantos pré-requisitos cada curso possui). O algoritmo de Khan funciona eliminando do grafo os nós que possuem grau de entrada 0 (que não possuem pré-requisitos) e atualizando os seus vizinhos (após cada remoção, atualiza o grau de entrada dos vizinhos). Apliquei esse comportamento usando como estrutura auxiliar uma fila `nextToAdd` e salvei os resultados de cada eliminação num array de resultado `res`. Ao final, confiro se todos os elementos foram incluídos no resultado e retorno. Caso alguns elementos tenham ficado de fora, isso indica que o grafo possui um ciclo (não é uma DAG), o que implica que não é possível realizar uma ordenação topológica adequada. Caso esse seja o caso, retorno uma lista vazia.

## Análise de complexidade
Para um problema com $v$ cursos e uma lista com $e$ pré-requisitos, tem-se:
- **Time complexity**: $O(v + e)$
- **Space complexity**: $O(v + e)$