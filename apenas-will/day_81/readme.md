## Exercício: 11. Container With Most Water
**Objetivo**: Dado uma lista de inteiros que representa altura de colunas, determine qual é o maior volume de água que pode ser obtido ao "inundar" o espaço entre duas colunas removendo as demais (suponha a lista [2, 2, 3] que indica que a altura de 3 colunas; se colocarmos água entre a primeira e segunda coluna, obtemos um total de 2; porém, se colocarmos entre a primeira e terceira, obtemos um total de 4).

## Descrição geral da estratégia
Para resolver adiciono dois ponteiros no array, um no início e um no final. A cada iteração de um loop, enquanto os dois ponteiros forem diferentes, calculo o volume de área, que é igual a altura da menor coluna multiplicado pelo diferença na posição das duas colunas ( $V(\text{lo}, \text{hi}) = \text{min(altura[lo], altura[hi])} \cdot (\text{hi} - \text{lo})$ ). Se o valor encontrado for maior que o maior valor encontrado até o momento, substituo o maior valor por esse, mantendo-o inalterado caso contrário. Em seguida, movo o ponteiro que está na posição de menor altura dos dois, na esperança de que o valor possa melhorar. Os passos anteriores se repetem até os ponteiros se encontrarem. Por fim, retorno o maior valor encontrado.   

## Análise de complexidade
Para uma array com $n$ inteiros, tem-se:
- **Time complexity**: $O(n)$
- **Space complexity**: $O(1)$ 