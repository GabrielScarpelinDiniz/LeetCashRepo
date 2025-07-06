## Exercício: 547. Number of Provinces
**Objetivo**: Dada uma matriz que indica se duas cidades possuem conexão entre si, quantas províncias existem. Uma província é definida como um conjunto de cidades que possuem um caminho que as conecte;

## Descrição geral da estratégia
Para resolver usei a matriz dada como uma matriz de adjacência de um grafo e apliquei DFS nas cidades. Nesse sentido, para cada cidade, confiro se ela já foi visitada. Se ela não tiver sido visitada, aplico o DFS que vai marcar como visitadas todas as cidades que eu consigo chegar a partir dessa e, em seguida, incremento em 1 a contagem de províncias. Repito o processo para todas as cidades não visitadas e, ao final, retorno o resultado da contagem;

## Análise de complexidade
Para um matriz $n \times n$, tem-se:
- **Time complexity**: $O(n)$
- **Space complexity**: $O(n)$ (considerando apenas espaço auxiliar)