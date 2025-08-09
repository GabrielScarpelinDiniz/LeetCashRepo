## Exercício: 40. Combination Sum II
**Objetivo**: Dado um array de inteiros e um inteiro target, retorne uma lista com todas as combinações únicas de elementos que a soma é igual ao target.

## Descrição geral da estratégia
Para resolver utilizo uma estratégia de backtracking usando um `Map` auxiliar de contagem dos elementos para tratar as duplicatas. Inicialmente, crio um `HashMap` que armazena os elementos no array inicial e a contagem de suas aparições. Em seguida, implemento a função de backtracking. Tal função adiciona uma combinação de elementos que a soma é igual ao target na variável de resultado `res`, explorando as chaves do `HashMap` para criar novas combinações (um elemento é adicionado se sua contagem for maior que 0. Após o uso, a contagem de um elemento é decrementada em 1, enquanto no backtrack de uma opção sua contagem é incrementada em 1). Para evitar que a ordem dos elemento afete as combinações, adicionei uma condicional que impede que um elemento menor seja colocado após um maior (forço a ordenação para evitar que ocorram duas combinações iguais com elementos em ordens distintas). Por fim, retorno a lista de combinações `res`.

## Análise de complexidade
Para um array com $n$ elementos candidatos, tem-se:
- **Time complexity**: $O(2^n)$ 
- **Space complexity**: $O(n)$
