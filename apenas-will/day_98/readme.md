## Exercício: 47. Permutations II
**Objetivo**: Dado um array de inteiros contendo duplicatas, retorne todas as permutações (array obtido a partir do array original trocando as posições dos elementos) únicas que podem ser geradas a partir do array.

## Descrição geral da estratégia
Para resolver uso uma abordagem de backtracking sobre um `HashMap` da contagem de elementos. Inicialmente, crio um `Map` que armazena quantas vezes cada elemento se repete. Em seguida, faço uma implementação padrão de backtracking que, em vez de iterar sobre o array original, itera sobre as chaves do `HashMap` averiguando quantas vezes elas foram utilizadas. Se uma chave tiver contagem maior que 0, significa que ainda pode-se utilizá-la no código, então cria-se uma permutação utilizando-a, decrementa-se 1 em sua contagem (como que removendo-a) e chama-se a função de backtracking novamente. Com isso, tratasse as chaves não como elementos únicos (como ocorre no array), mas como elementos que possuem cópias, evitando duplicatas (por exemplo, tendo uma array inicia [**1**, _1_], observe o elemento em negrito e em itálico. Se tratarmos cada elemento como único, obteríamos como output [[**1**, _1_], [_1_, **1**]]. Entretanto, usa-se o `HashMap` para remover esse tratamento dos elementos, como se não fizéssemos distinção entre os elementos iguais). Armazeno todas as combinações em uma lista `res` que é retornada ao final. 

## Análise de complexidade
Para um array com $n$ inteiros, tem-se:
- **Time complexity**: $O(2^n)$ 
- **Space complexity**: $O(2^n)$
