## Exercício: 1470. Shuffle the Array
**Objetivo**: Dada uma array de inteiros, divida o array em dois e intercale seus elementos em um novo array.

## Descrição geral da estratégia
Para resolver, implemento o comportamento descrito. Para tal imagino um array com tamanho igual a metade do array original no qual eu adiciono pares de elementos. Com essa ideia em mente, implemento um loop que adiciona dois elementos por vez no array de resultado (sendo um dos elementos adicionados da primeira metade do array original e outro da segunda metade). Sigo esse processo até o final do array original, retornando o resultado ao final.

## Análise de complexidade
Para um array com $n$ elementos, tem-se:
- **Time complexity**: $O(n)$ 
- **Space complexity**: $O(n)$
