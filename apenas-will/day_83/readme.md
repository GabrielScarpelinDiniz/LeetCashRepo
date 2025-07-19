## Exercício: 24. Swap Nodes in Pairs
**Objetivo**: Dado o nó inicial de uma lista ligada, retorne a mesma lista mas com os nós trocados em pares ( imagine uma lista $1 \rightarrow 2 \rightarrow 3$, o output seria $2 \rightarrow 1 \rightarrow 3$, no qual os pares foram trocados).

## Descrição geral da estratégia
Para resolver faço a troca de um elemento pelo próximo elemento na lista. Em seguida, faço com que o segundo elemento do par (que antes era o primeiro) receba como seguinte o resultado da troca do próximo par. Isso continua de maneira recursiva até o final da lista.
   
## Análise de complexidade
Para uma lista com $n$ nós, tem-se:
- **Time complexity**: $O(n)$ 
- **Space complexity**: $O(n)$ 