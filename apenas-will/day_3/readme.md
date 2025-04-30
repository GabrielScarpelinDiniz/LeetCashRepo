## Exercício: 206. Reverse Linked List
**Objetivo**: Dada uma lista encadeada, inverta a ordem dos elementos;

## Descrição geral da estratégia
Usei uma abordagem iterativa, estabelecendo três nós âncoras (prev, current e next) e alterando a referência do current para o prev a cada iteração. 

## Análise de complexidade
Para uma lista de $n$ nós, tem-se:
- **Time complexity**: $O(n)$
- **Space complexity**: $O(1)$