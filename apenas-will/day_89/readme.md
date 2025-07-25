## Exercício: 300. Longest Increasing Subsequence
**Objetivo**: Dado um array de inteiros, retorne o tamanho da maior subsequência crescente. Uma subsequência de um array é definida como um outro array que pode ser obtido após a deleção de um ou mais elementos.

## Descrição geral da estratégia
Para resolver usei uma abordagem de programação dinâmica. Primeiro crio um array auxiliar que armazenará a maior subsequência até determinado índice (`maxAt[i]` armazena a maior subsequência até o elemento `i`, sendo inicializada como um array com 1 em todas as posições). Em seguida, para cada índice do array original, confiro os elementos anteriores a ele que possuem um valor menor que o próprio elemento. Caso eu encontre um elemento com essas características, confiro qual é o comprimento da maior subsequência até esse valor e, se esse valor for maior que o comprimento atual, substituo o comprimento atual por esse valor + 1 (como que indicando que a sequência agora tem um novo elemento). Repito esse processo até o final, salvando o maior elemento global (conferido a cada iteração do loop). Ao final, retorno o máximo global.

## Análise de complexidade
Para um array com $n$ inteiros, tem-se:
- **Time complexity**: $O(n^2)$ 
- **Space complexity**: $O(n)$
