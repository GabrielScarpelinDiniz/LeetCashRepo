## Exercício: 26. Remove Duplicates from Sorted Array
**Objetivo**: Dado um array de inteiros ordenado, retorne o número de elementos únicos nesse array **e** remova as duplicatas do array original (para linguagens que arrays não são estruturas dinâmicas, apenas mova os elementos para o início e o código irá ignorar o resto).

## Descrição geral da estratégia
Para resolver utilizo dois ponteiros, ambos posicionados, inicialmente, no começo do array. Em seguida, itero pelo array, mantendo um ponteiro fixo e comparando sempre se os valores em cada um das posições dos ponteiros são diferentes. Se forem, então eu incremento em 1 o ponteiro que estava fixo e modifico o elemento dessa posição por aquele encontrado pelo array mais adiante. Também incremento uma variável `k`, que deve ser retornada ao final do código. Repito o processo anterior até chegar ao final do array, retornando `k` após o loop.
   
## Análise de complexidade
Para um array com $n$ inteiros, tem-se:
- **Time complexity**: $O(n)$ 
- **Space complexity**: $O(1)$ 