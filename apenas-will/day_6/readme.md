## Exercício: 70. Climbing Stairs
**Objetivo**: Dada uma escada de $n$ degraus, determine quantos jeitos distintos é possível subir essa escada, sabendo que você pode, a cada degrau, decidir subir 1 ou 2 degraus;

## Descrição geral da estratégia
Fiz alguns testes para alguns tamanhos de escada para ver se ela seguia algum padrão e percebi que o número de possibilidades seguia a sequência de Fibonacci. Com isso, só implementei a função de Fibonacci.

## Análise de complexidade
Para uma escada com $n$ degraus, tem-se:
- **Time complexity**: $O(n)$ 
- **Space complexity**: $O(n)$, (por causa do memoization)
