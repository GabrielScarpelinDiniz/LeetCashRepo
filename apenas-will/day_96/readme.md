## Exercício: 45. Jump Game II
**Objetivo**: Dado um array de inteiros que indica quantas casas se pode pular a partir desse ponto, determine o número mínimo de saltos necessários para alcançar a última casa.

## Descrição geral da estratégia
Para resolver utilizo uma abordagem de programação dinâmica que vai progressivamente salvando a quantidade mínima de saltos para se chegar a determinada posição. Nesse sentido, crio um array auxiliar que armazenará o número mínimo de saltos necessários para se chegar a cada posição e o inicializo com `Integer.MAX_VALUE`. Em seguida, itero pelo array de inteiros original e vou atualizando o mínimo necessário para se chegar às posições que se pode alcançar a partir dele (salvo o mínimo entre o elemento que já estiver nessa posição e o valor presente na "posição de salto" + 1). Continuo o processo até o último elemento e retorno o último elemento de `jumpsToReach`.

## Análise de complexidade
Para um array com $n$ elementos, tem-se:
- **Time complexity**: $O(n^2)$ 
- **Space complexity**: $O(n)$
