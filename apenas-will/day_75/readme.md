## Exercício: 78. Subsets
**Objetivo**: Dado array de inteiros, retorne uma lista contendo todos os subconjuntos que podem ser formados com esses inteiros (a ordem dos elementos nos subconjuntos não importa e a lista não contém duplicatas).

## Descrição geral da estratégia
Para resolver aplico um algoritmo de backtracking que vai criando os subconjuntos pouco a pouco. Primeiro, é criado o subconjunto vazio, em seguida, todos os subconjuntos contendo o primeiro elemento, depois o segundo, terceiro e assim por diante até o final.

## Análise de complexidade
Para uma array com $n$ inteiros, tem-se:
- **Time complexity**: $O(2 \cdot 2^n)$
- **Space complexity**: $O(2^n)$ 